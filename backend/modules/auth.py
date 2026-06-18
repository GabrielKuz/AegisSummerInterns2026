from typing import Annotated
import os
from dotenv import load_dotenv

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from jwt import PyJWKClient, decode
from pydantic import BaseModel

load_dotenv()

TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
JWKS_URL = f"https://login.microsoftonline.com/{TENANT_ID}/discovery/v2.0/keys"
ISSUER = f"https://login.microsoftonline.com/{TENANT_ID}/v2.0"

if not CLIENT_ID:
    raise ValueError("CLIENT_ID environment variable is required for Entra ID SSO")

jwks_client = PyJWKClient(JWKS_URL)

scheme = OAuth2PasswordBearer(tokenUrl="token")

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    disabled: bool | None = None



async def getCurrentUser(token: Annotated[str, Depends(scheme)]):
    credentialsException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        signingKey = jwks_client.get_signing_key_from_jwt(token).key # get singing key fropm ms jwks endpoint
        
        payload = decode( #decode and validate
            token,
            signingKey,
            algorithms=["RS256"],
            audience=CLIENT_ID,
            issuer=ISSUER,
        )
        
        username: str = payload.get("preferred_username") or payload.get("upn") or payload.get("oid")
        if username is None:
            raise credentialsException
        
        tokenData = TokenData(username=username)
    except InvalidTokenError as e:
        raise credentialsException
    except Exception as e:
        raise credentialsException
    
    return User(username=tokenData.username, disabled=False)

async def getCurrentActiveUser(current_user: Annotated[User, Depends(getCurrentUser)]):
    if current_user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
    return current_user

