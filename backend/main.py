from fastapi import FastAPI, Depends
from typing import Annotated

from modules.downloadData import downloadData
from modules.auth import getCurrentUser, User, getCurrentActiveUser

app = FastAPI(title="Aegis Backend", root_path="/api")

@app.get("/")
def read_root():
    return {"status": "ok"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

def main():
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)

@app.get("/links/{uuid}/download")
def download_link(uuid: str, currentUser: Annotated[User, Depends(getCurrentActiveUser)]):
    return downloadData(uuid, currentUser)

if __name__ == "__main__":
    main()
    