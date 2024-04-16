"""
Response model to standardise response from server to client.
"""
from pydantic import BaseModel  # pylint: disable = no-name-in-module


class AddAddress(BaseModel):  # pylint: disable=too-few-public-methods
    """
    AddAddress model contains
    status: Success/Failed indicates the status of an API call.
    message: will contain the additional information.
    """
    address: str
    latitude: float
    longitude: float
