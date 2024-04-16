from pydantic import BaseModel


class UpdateAddress(BaseModel):
    """
    UpdateAddress model contains details for updating an address.

    Attributes:
        id (int): The unique identifier for the address.
        address (str | None): The updated address string. Can be None if not available.
        latitude (float | None): The updated latitude coordinate of the address. Can be None if not available.
        longitude (float | None): The updated longitude coordinate of the address. Can be None if not available.
    """
    id: int
    address: str | None
    latitude: float | None
    longitude: float | None
