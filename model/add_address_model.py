"""
Response model to standardise response from server to client.
"""
from pydantic import BaseModel

class AddAddress(BaseModel):
    """
    AddAddress model contains
    status: Success/Failed indicates the status of an API call.
    message: will contain the additional information.
    """
    address: str
    latitude: float
    longitude: float
