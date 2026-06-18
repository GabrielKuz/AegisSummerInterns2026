from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from modules.auth import getCurrentActiveUser, User

app = FastAPI(title="Aegis Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # TODO: add real urls later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"status": "ok", "message": "Aegis Backend is running"}


@app.get("/auth/me")
async def get_current_user(current_user: Annotated[User, Depends(getCurrentActiveUser)]):
    return {
        "username": current_user.username,
        "disabled": current_user.disabled,
    }


@app.get("/health")
def health_check(current_user: Annotated[User, Depends(getCurrentActiveUser)]):
    return {"status": "healthy"}

def main():
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)


if __name__ == "__main__":
    main()
