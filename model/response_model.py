from pydantic import BaseModel  # pylint: disable = no-name-in-module


class ResponseModel(BaseModel):  # pylint: disable=too-few-public-methods
    """
    Response model contains
    status: Success/Failed indicates the status of an API call.
    message: will contain the additional information.
    """
    status: str
    message: str | dict
    object: dict | None
