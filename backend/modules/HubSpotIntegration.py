from hubspot import HubSpot
from hubspot.crm.contacts import SimplePublicObjectInputForCreate
from hubspot.oauth import ApiException
from pathlib import Path
from typing import Iterable

api_client = HubSpot(access_token='your_access_token')

# or set your access token later
# api_client = HubSpot()
# api_client.access_token = 'your_access_token'

def get_accessToken():
    try:
        tokens = api_client.oauth.tokens_api.create(
            grant_type = "authorization_code",
            redirect_uri = 'http://localhost',
            client_id = 'client_id',
            client_secret = 'client_secret',
            code = 'code'
        )
    except ApiException as e:
        print("Exception when calling create_token method: %s\n" % e)

def get_caseID() -> String:

def get_caseStatus(caseID: str) -> type:

def is_caseExpirable(caseID: str) -> bool:



#def send_emailForSupport() -> void:
#    try:
#        simple_public_object_input_for_create = SimplePublicObjectInputForCreate(
#            properties = {"email":""}
#            #              ^ Email for support ^
#        )
#       api_response = api_client.crm.contacts.basic_api.create(
#            simple_public_object_input_for_create=simple_public_object_input_for_create
#        )
#    except ApiException as e:
#        print("Exception when creating contact: %s\n" % e)


