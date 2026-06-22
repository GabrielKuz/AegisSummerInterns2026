from pathlib import Path
from typing import Annotated

from fastapi import APIRouter, File, UploadFile

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/files/")
async def create_file(
    file: Annotated[bytes | None, File(description="A file read as bytes")] = None,
):
    if file is None:
        return {"message": "No file present"}
    return {"file_size": len(file)}


@router.post("/uploadfile/")
async def create_upload_file(
    file: Annotated[UploadFile | None, File(description="A file read as UploadFile")] = None,
):
    if file is None:
        return {"message": "No upload file sent"}

    contents = await file.read()
    destination = UPLOAD_DIR / Path(file.filename).name

    with destination.open("wb") as f:
        f.write(contents)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(contents),
        "path": str(destination),
    }


def get_file_size(file: UploadFile) -> int:
    file.file.seek(0, 2)
    size = file.file.tell()
    file.file.seek(0)
    return size


def get_file_type(file: UploadFile):
    return file.content_type


def get_file_name(file: UploadFile):
    return file.filename




