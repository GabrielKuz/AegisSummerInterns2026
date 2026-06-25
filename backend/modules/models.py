from sqlalchemy import UUID, BigInteger, Column, String, Integer, DateTime, Boolean, Text, JSON
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import declarative_base

Base = declarative_base()

import uuid

class UploadRecord(Base):
    __tablename__ = "uploads"
    __table_args__ = {"schema": "LinkDB"}
    upload_id: Column[UUID] = Column(UUID(as_uuid=False), primary_key=True, default=lambda: str(uuid.uuid4()))
    link_uuid: Column[UUID] = Column(UUID(as_uuid=False), nullable=False, index=True)
    original_filename: Column[Text] = Column(Text, nullable=True)
    blob_name: Column[Text] = Column(Text, nullable=True)
    content_type: Column[Text] = Column(Text, nullable=True)
    sha256: Column[Text] = Column(Text, nullable=True)
    date_uploaded: Column[DateTime] = Column(DateTime, nullable=False)
    itar_status: Column[Boolean] = Column(Boolean, default=False)
    combined_file_size: Column[BigInteger] = Column(BigInteger)
    timestamp: Column[DateTime] = Column(DateTime)
    max_days_in_storage: Column[Integer] = Column(Integer, default=30)
    case_id: Column[String] = Column(String, nullable=True)
    original_link: Column[Text] = Column(Text, nullable=True)
    sas_retrieval_link: Column[Text] = Column(Text, nullable=True)
    upload_complete: Column[Boolean] = Column(Boolean, default=False)
    users_with_access: Column[JSONB] = Column(JSONB, nullable=True)


class LinkRecord(Base):
    __tablename__ = "links"
    __table_args__ = {"schema": "LinkDB"}
    uuid: Column[UUID] = Column(UUID(as_uuid=False), primary_key=True)
    link: Column[String] = Column(String)
    case_id: Column[String] = Column(String)
    creator: Column[String] = Column(String)
    timestamp: Column[DateTime] = Column(DateTime)
    itar:Column[Boolean] = Column(Boolean)
    users_with_access:Column[JSONB] = Column(JSONB)
    expired:Column[Boolean] = Column(Boolean)
