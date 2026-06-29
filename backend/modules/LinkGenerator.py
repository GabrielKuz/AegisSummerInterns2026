from fastapi import HTTPException, status
from pydantic import BaseModel, Field
import uuid
from datetime import datetime, timedelta
from sqlalchemy import create_engine, select, update
from typing import Dict
from modules.auth import User
from modules.models import LinkRecord
import os
from modules import Session, engine

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
    raise RuntimeError("DATABASE_URL environment variable is required")

class LinkRequest(BaseModel):
    case_id: str = Field(..., description="ID of the case associated with the link")
    itar: bool = Field(..., description="Indicates if the link is ITAR compliant")


link_data: Dict[str, LinkRequest] = {}

url = f"{os.getenv('BACKEND_URL')}/backend/links/"


def generate_links(link_request: LinkRequest, current_user: User):
    if not current_user or current_user.disabled:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not authenticated"
        )

    uuid_str = str(uuid.uuid4())

    store_link(link_request, uuid_str, current_user)

    return {
        "link": url + uuid_str,
        "uuid": uuid_str
    }


def store_link(link_request: LinkRequest, uuid_str: str, current_user: User):
    with Session() as session:
        record = LinkRecord(
            uuid=uuid_str,
            link=url + uuid_str,
            case_id=link_request.case_id,
            itar=link_request.itar,
            creator=current_user.username,
            timestamp=datetime.now(),
            expiration_date=datetime.now() + timedelta(days=2),
            users_with_access=[current_user.username],
            expired=False,
        )

        # print("TABLE:", LinkRecord.__table__)
        # print("SCHEMA:", LinkRecord.__table__.schema)
        # print("FULLNAME:", LinkRecord.__table__.fullname)

        session.add(record)
        session.commit()


def get_all_links(current_user: User):
    if not current_user or current_user.disabled:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not authenticated"
        )
    with Session() as session:
        stmt = select(LinkRecord).where(LinkRecord.creator == current_user.username)
        records = session.scalars(stmt).all()
        result = []
        for r in records:
            result.append({
                "uuid": r.uuid,
                "link": r.link,
                "case_id": r.case_id,
                "itar": r.itar,
                "creator": r.creator,
                "timestamp": r.timestamp,
                "expiration_date": r.expiration_date,
                "users_with_access": r.users_with_access,
                "expired": r.expired,
            })

        return result