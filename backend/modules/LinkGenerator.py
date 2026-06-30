from fastapi import HTTPException, status
from pydantic import BaseModel, Field
import uuid
from datetime import datetime, timedelta
from sqlalchemy import create_engine, select, update
from typing import Dict
from modules.auth import User
from modules.models import LinkRecord, UploadRecord
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
    """
    Generates link and UUID and assigns them to the provided case ID and ITAR status. 
    Stores the link in the database.
    """
    if not current_user or current_user.disabled:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not authenticated"
        )
    
    if not link_request.case_id.startswith("AIS-") and not link_request.case_id[link_request.case_id.index("-")+1:].isdigit():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid Case-ID: Bad Request"
        )

    uuid_str = str(uuid.uuid4())

    store_link(link_request, uuid_str, current_user)

    if not url or not uuid_str:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Link or UUID not found"
        )

    return {
        "link": url + uuid_str,
        "uuid": uuid_str
    }


def store_link(link_request: LinkRequest, uuid_str: str, current_user: User):
def store_link(link_request: LinkRequest,uuid_str: str, current_user: User):
    """
    Stores the generated link and UUID in the database with associated case ID, 
    ITAR status, creator, timestamp, users with access, expiration date, and expiration status.
    """
    print("STORE_LINK CALLED", uuid_str)

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

        print(repr(record))
        session.add(record)
        rows = session.query(LinkRecord).filter(LinkRecord.uuid == record.uuid).all()
        print("DB rows for uuid:", rows)
        session.commit()



#         for record in records:
#             if not record.timestamp:
#                 continue

#             try:
#                 ts_dt = record.timestamp
#             except Exception:
#                 continue

#             if ts_dt <= cutoff:
#                 record.expired = True
#             else:
#                 record.expired = False

#         session.commit()

# def extend_link_expiration(uuid_str: str, current_user: User, extension: int):
#     """
#     Extends expiration date by specified number of days for a specific link
#     """
#     if not current_user or current_user.disabled:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="User not authenticated"
#         )

#     with Session() as session:
#         stmt = select(LinkRecord).where(LinkRecord.uuid == uuid_str)
#         record = session.scalar(stmt)

#         if not record:
#             raise HTTPException(
#                 status_code=status.HTTP_404_NOT_FOUND,
#                 detail="Link not found"
#             )

#         if record.creator != current_user.username:
#             raise HTTPException(
#                 status_code=status.HTTP_403_FORBIDDEN,
#                 detail="You do not have permission to extend this link"
#             )
        
#         if extension <= 0 or not isinstance(extension, int):
#             raise HTTPException(
#                 status_code=status.HTTP_400_BAD_REQUEST,
#                 detail="Extension must be a positive integer"
#             )

#         expire_old_links(expiry_days=extension)
#         session.commit()

def _serialize_link_record(record: LinkRecord):
    expiration_date = None
    if record.timestamp is not None:
        expiration_date = (record.timestamp + timedelta(days=2))

    return {
        "uuid": record.uuid,
        "link": record.link,
        "case_id": record.case_id,
        "itar": record.itar,
        "creator": record.creator,
        "timestamp": record.timestamp,
        "users_with_access": record.users_with_access,
        "expired": record.expired,
        "expiration_date": expiration_date,
    }


def get_link_by_uuid(uuid_str: str, current_user: User):
    """
    Retrieves a single link from the database by UUID.
    """
    if not current_user or current_user.disabled:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not authenticated"
        )
    if not uuid_str:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Link UUID not found"
        )

    with Session() as session:
        stmt = select(LinkRecord).where(LinkRecord.uuid == uuid_str)
        record = session.scalar(stmt)
        if record is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Link not found"
            )
        return _serialize_link_record(record)

        if record.creator != current_user.username:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to extend this link"
            )
        
        if extension <= 0 or not isinstance(extension, int):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Extension must be a positive integer"
            )

        record.expiration_date += timedelta(days=extension)
        record.expired = False
        session.commit()

def get_link(uuid_str: str):
    with Session() as session:
        stmt = select(LinkRecord).where(LinkRecord.uuid == uuid_str)
        record = session.scalar(stmt)
        if not record:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Link not found")

        return {
            "uuid": record.uuid,
            "link": record.link,
            "case_id": record.case_id,
            "itar": record.itar,
            "creator": record.creator,
            "timestamp": record.timestamp,
            "expiration_date": record.expiration_date,
            "users_with_access": record.users_with_access,
            "expired": record.expired,
        }

def get_all_links(current_user: User):
    """
    Retrieves all links from the database and returns them as a list of dictionaries.
    """
    if not current_user or current_user.disabled:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not authenticated"
        )
    with Session() as session:
        stmt = select(LinkRecord).where(LinkRecord.creator == current_user.username)
        records = session.scalars(stmt).all()
        return [_serialize_link_record(r) for r in records]
    
def get_all_files_for_link(uuid_str: str, current_user: User):
    """
    Gets all file names and data from a specific link UUID.
    """
    if not current_user or current_user.disabled:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not authenticated"
        )
    if not uuid_str:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Link UUID not found"
        )
    with Session() as session:
        stmt1 = select(LinkRecord).where(LinkRecord.uuid == uuid_str)
        link_record = session.scalar(stmt1)
        if link_record is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Link not found"
            )
        if link_record.expired:
            raise HTTPException(
                status_code=status.HTTP_410_GONE,
                detail="Associated link is expired"
            )
        stmt2 = select(UploadRecord).where(UploadRecord.link_uuid == uuid_str)
        records = session.scalars(stmt2).all()
        result = []
        for r in records:
            if (r.timestamp - datetime.now()).days >= r.max_days_in_storage:
                raise HTTPException(
                    status_code=status.HTTP_410_GONE,
                    detail="Associated data is expired"
                )
            result.append({
                "upload_id": r.upload_id,
                "filename": r.original_filename,
                "file_name": r.original_filename,
                "size": r.combined_file_size,
                "blob_name": r.blob_name,
                "content_type": r.content_type,
                "date_uploaded": r.date_uploaded
            })
        return result
    