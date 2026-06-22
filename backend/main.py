from fastapi import FastAPI, Depends
from modules.LinkGenerator import LinkRequest, generate_links
from modules.auth import getCurrentActiveUser, User
from modules.uploader import router as uploader_router
from typing import Annotated

app = FastAPI(title="Aegis Backend")
app.include_router(uploader_router)

@app.post("/links/create/")
def create_link(link_request: LinkRequest):
    return generate_links(link_request)

@app.get("/")
def read_root():
    return {"status": "ok"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/auth/me")
def get_current_user(user: Annotated[User, Depends(getCurrentActiveUser)]):
    return {"username": user.username, "disabled": user.disabled}



def main():
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)


if __name__ == "__main__":
    main()
    import os
    from azure.storage.blob import BlobServiceClient

    connection_string = os.environ["AZURE_STORAGE_CONNECTION_STRING"]

    print("Connecting to storage...")

    blob_service = BlobServiceClient.from_connection_string(
        connection_string
    )

    # Create test container
    container_name = "test-container"

    try:
        blob_service.create_container(container_name)
        print(f"Created container: {container_name}")
    except Exception as e:
        print(f"Container may already exist: {e}")

    # Upload test blob
    blob_client = blob_service.get_blob_client(
        container=container_name,
        blob="hello.txt"
    )

    content = b"Hello from Azurite!"

    blob_client.upload_blob(content, overwrite=True)
    print("Uploaded blob")

    # Download blob
    downloaded = blob_client.download_blob().readall()

    print("Downloaded blob contents:")
    print(downloaded.decode())

    # List containers
    print("\nContainers:")
    for container in blob_service.list_containers():
        print(f" - {container['name']}")

    print("\nSUCCESS")
