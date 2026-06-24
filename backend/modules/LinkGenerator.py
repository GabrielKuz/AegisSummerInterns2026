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
    case_id: str = Field(
        ...,
        description="ID of the case associated with the link"
    )


link_data: Dict[str, LinkRequest] = {}

url = f"http://{os.getenv('BACKEND_URL')}/backend/links/"


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


def store_link(link_request: LinkRequest,uuid_str: str, current_user: User):
    print("STORE_LINK CALLED", uuid_str)

    with Session() as session:
        record = LinkRecord(
            uuid=uuid_str,
            link=url + uuid_str,
            case_id=link_request.case_id,
            creator=current_user.username,
            timestamp=datetime.now(),
            users_with_access=[current_user.username],
            expired=False
        )

        # print("TABLE:", LinkRecord.__table__)
        # print("SCHEMA:", LinkRecord.__table__.schema)
        # print("FULLNAME:", LinkRecord.__table__.fullname)

        session.add(record)
        session.commit()


def expire_old_links():
    cutoff = datetime.now() - timedelta(days=2)

    with Session() as session:
        stmt = select(LinkRecord).where(
            (LinkRecord.expired == False) |
            (LinkRecord.expired.is_(None))
        )

        records = session.scalars(stmt).all()

        for record in records:
            if not record.timestamp:
                continue

            try:
                ts_dt = record.timestamp
            except Exception:
                continue

            if ts_dt <= cutoff:
                record.expired = True

        session.commit()