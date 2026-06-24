from fastapi import FastAPI, Depends, HTTPException
from modules.LinkGenerator import LinkRequest, generate_links
from modules.auth import getCurrentActiveUser, getCurrentUser, User, userAuthenticated, getCurrentUserNoAuthForTest
from modules.uploader import router as uploader_router, listFiles
from modules.downloadData import downloadData
from typing import Annotated
from warnings import deprecated

app = FastAPI(title="Aegis Backend", root_path="/api")
app.include_router(uploader_router)

@app.post("/links/create/")
def create_link(link_request: LinkRequest, current_user: Annotated[User, Depends(getCurrentUserNoAuthForTest)]):
    #authentication: bool = userAuthenticated(getCurrentUser())
    return generate_links(link_request, current_user) #TODO: CHANGE IMMENDIATLY AFTER TESTING

@app.get("/")
def read_root():
    return {"status": "ok"}


def main():
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)

@app.get("/links/{uuid}/download")
@deprecated("use /uploads/{upload_id}/download instead. This assumes only one uploaded file per link")
def download_link(uuid: str, currentUser: Annotated[User, Depends(getCurrentUserNoAuthForTest)]):
    uploads = listFiles(uuid)
    if len(uploads) == 1:
        return downloadData(uploads[0]["upload_id"], currentUser)
    if not uploads:
        raise HTTPException(status_code=404, detail="No uploads found for this link")
    return uploads


@app.get("/uploads/{upload_id}/download")
def download_upload(upload_id: str, currentUser: Annotated[User, Depends(getCurrentUserNoAuthForTest)]):
    return downloadData(upload_id, currentUser)

if __name__ == "__main__":
    main()
