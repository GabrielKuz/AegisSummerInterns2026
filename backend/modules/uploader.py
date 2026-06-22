from pathlib import Path
from typing import Annotated
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import datetime
import hashlib

from fastapi import APIRouter, File, UploadFile

from .Ekeys import createEncryptKey

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/uploadfile/") # Define a POST endpoint at the path "/uploadfile/" that allows clients to upload files. The function create_upload_file will handle the incoming file data as an UploadFile object, which provides more metadata and functionality compared to raw bytes.
async def create_upload_file(
    file: Annotated[UploadFile | None, File(description="A file read as UploadFile")] = None, # Define the file parameter, which would be automatically read as an UploadFile by FastAPI. If no file is provided, it defaults to None. And a description is added to the File for possibly some connection to the front end.
):
    if file is None: # If no file is provided, return a message indicating that no upload file is sent.
        return {"message": "No upload file sent"}

    contents = await file.read() # If file is present it will read it and upload to the path

    destination = UPLOAD_DIR / Path(file.filename).name # Creates destination path but does not 
    if destination.exists():
        path_obj = Path(file.filename) # Makes a path from the name to grab the stem from later
        stem = path_obj.stem # gets the file name without the extension
        suffix = path_obj.suffix # gets the file name extension
        counter = 1 # duplicate counter starts at 1

        while destination.exists(): # If the destination already exists (E.g. a file with the same name already exists)
            if suffix:
                destination = UPLOAD_DIR / f"{stem}_{counter}{suffix}" # if suffix is present then it will check for duplicates with same stem, counter, and suffix
            else:
                destination = UPLOAD_DIR / f"{stem}_{counter}" # if no suffix is present then it will check for duplicates with same stem and counter only
            counter += 1 # increases counter further if another clone exists

    padder = padding.PKCS7(algorithms.AES256.block_size).padder()
    padded_data = padder.update(contents) + padder.finalize()

    cipher = Cipher(algorithms.AES256())

    
    with destination.open("wb") as f:
        f.write(contents)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(contents),
        "path": str(destination),
        "date and time": str(datetime.datetime.now()),
    }

