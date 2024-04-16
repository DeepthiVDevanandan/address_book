from pydantic import BaseModel  # pylint: disable = no-name-in-module


class GetAddress(BaseModel):  # pylint: disable=too-few-public-methods
    """
    GetAddress model contains details of a single address.

    Attributes:
        id (int): The unique identifier for the address.
        address (str | None): The address string. Can be None if not available.
        latitude (float | None): The latitude coordinate of the address. Can be None if not available.
        longitude (float | None): The longitude coordinate of the address. Can be None if not available.
    """
    id: int
    address: str | None
    latitude: float | None
    longitude: float | None


class SearchInputs(BaseModel):
    """
    SearchInputs model contains inputs for searching addresses.

    Attributes:
        longitude (float): The longitude coordinate for the search.
        latitude (float): The latitude coordinate for the search.
        distance (float): The maximum distance within which to search for addresses.
    """
    longitude: float
    latitude: float
    distance: float
