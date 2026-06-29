import os
from typing import Optional

from hubspot import HubSpot
from hubspot.crm.tickets import ApiException
from hubspot.crm.tickets.models import Filter, FilterGroup, PublicObjectSearchRequest

api_client = HubSpot(access_token=os.getenv("HUBSPOT_ACCESS_TOKEN"))


def get_caseID(ais_id: str) -> Optional[str]:
    ...

def get_caseStatus(ais_id: str) -> Optional[str]:
    ...

def is_caseExpirable(ais_id: str) -> bool:
    ...


def get_ticket(ais_id: str):
    ...