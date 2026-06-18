from LinkGenerator import LinkRequest, generate_links
from pydantic import BaseModel, Field
from pathlib import Path

class ReceiptRequest(BaseModel):
    user_id: str = Field(..., description="ID of the user for whom the receipt is being generated")
    case_id: str = Field(..., description="ID of the case associated with the receipt")
    timestamp: str = Field(..., description="The timestamp when the receipt is generated")
    itar: bool = Field(..., description="Whether the receipt is ITAR compliant")
    log_path: Path = Field(..., description="The path to the log file")

def generate_receipt(receipt_request: ReceiptRequest):
    if receipt_request.itar:
        itar_str = "ITAR"
    else:
        itar_str = "non-ITAR"
    with open("log.txt", "w") as log_file:
        log_file.write(f"{receipt_request.timestamp}: {receipt_request.user_id} accessed {itar_str} data at {receipt_request.log_path}\n")