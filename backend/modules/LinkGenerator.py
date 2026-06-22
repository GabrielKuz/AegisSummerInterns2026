from fastapi import HTTPException, status
from pydantic import BaseModel, Field
import uuid
from datetime import datetime
from modules.auth import getCurrentUser, userAuthenticated

class LinkRequest(BaseModel):
    case_id: str = Field(..., description="ID of the case associated with the link")

link_data: dict[str, LinkRequest] = {}

url: str = "http://localhost:8000/backend/links/" # base url for link generation, can be changed to actual domain when deployed

def generate_links(link_request: LinkRequest):
    if not userAuthenticated(getCurrentUser()):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not authenticated")
    
    if url is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Link generation failure")
    
    uuid_str = str(uuid.uuid4())
    return {"link": url + uuid_str, 
            "uuid": uuid_str}