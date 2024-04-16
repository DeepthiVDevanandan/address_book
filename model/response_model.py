from pydantic import BaseModel


class ResponseModel(BaseModel):
    """
    Response model contains
    status: Success/Failed indicates the status of an API call.
    message: will contain the additional information.
    """
    status: str
    message: str | dict
    object: dict | None
