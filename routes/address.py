"""
APIs for CRUD operations on address book application.
"""
# pylint: disable=broad-except, E0401
from fastapi import APIRouter
from model.get_address_model import GetAddress
from model.add_address_model import AddAddress
from model.update_address_model import UpdateAddress
from model.response_model import ResponseModel
from modules import address_api

router = APIRouter()


@router.post("/", response_model=ResponseModel)
def save_address(address: AddAddress):
    """
      API to add a new address to database.

      Parameters:
            -Holds address data.

      Returns:
          -Success or Failed message.
    """
    response = address_api.save_address(address)
    print('response', response)
    return response


@router.get("/", response_model=list[GetAddress])
def get_addresses(longitude: float, latitude: float, distance: float):
    """
           API to get addresses from database by searching criteria .

           Parameters:
           - search_criteria(SearchInputs): Hold search criteria .

           Returns:
           - List of GetAddress.
    """
    search_criteria = {"longitude": longitude, "latitude": latitude,
                       "distance": distance}
    response = address_api.get_address(search_criteria)
    return response


@router.patch("/")
def update_address(updated_address: UpdateAddress):
    """
       API to update address to the database.

       Parameters:
       - updated_address (UpdateAddress): Holds updated address data.

       Returns:
       - JSONResponse:  Success or Failed message.
    """
    response = address_api.update_address(updated_address)
    return response


@router.delete("/{address_id}/")
def delete_address(address_id: int):
    """
    API to delete an address from the database.

    Parameters:
        - address_id (int): The ID of the address to delete.

    Returns:
        - JSONResponse: Success or Failed message.
    """
    response = address_api.delete_address(address_id)
    return response
