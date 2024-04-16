"""
Functions to do CRUD operations on address application.
"""
# pylint: disable=broad-except, E0401
from datetime import datetime
import sqlite3
from fastapi import status
from fastapi.responses import JSONResponse
from common.db_connection import create_connection
from model.response_model import ResponseModel
from model.add_address_model import AddAddress
from model.get_address_model import SearchInputs
from model.update_address_model import UpdateAddress


def save_address(address: AddAddress):
    """
    Function to save an address to the database
    """
    try:
        created_date = datetime.now()
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO addresses (address, latitude, "
            "longitude, created_on) VALUES (?,?,?,?)",
            (address.address, address.latitude, address.longitude,
             created_date))
        address_id = cursor.lastrowid
        connection.commit()
        connection.close()
        if address_id > 0:
            return ResponseModel(
                status="Success", message="Address saved successfully",
                object={"id": address_id}
            )
    except sqlite3.Error as e:
        return handle_database_error(e)
    except Exception as e:
        return handle_general_error(e)


def update_address(address: UpdateAddress):
    """
    Function to update an existing address in the database
    """
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            """ UPDATE addresses SET address = ?, latitude = ?, longitude = ?
            WHERE id = ?""",
            (address.address, address.latitude, address.longitude, address.id))
        rows_updated = cursor.rowcount
        connection.commit()
        connection.close()
        if rows_updated > 0:
            return ResponseModel(
                status="Success", message="Address updated successfully",
                object={"id": address.id}
            )
        return ResponseModel(
                status="Failed", message="Address update failed, "
                                         "Address ID might not exist.",
                object={"id": address.id}
            )
    except sqlite3.Error as e:
        return handle_database_error(e)
    except Exception as e:
        return handle_general_error(e)


def delete_address(address_id):
    """
    Function to delete an address from the database
    """
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
                DELETE FROM addresses
                WHERE id = ?
            """,
            (address_id,))
        rows_affected = cursor.rowcount
        connection.commit()
        connection.close()
        if rows_affected > 0:
            return ResponseModel(
                status="Success", message="Address deleted successfully",
                object={"id": address_id}
            )
        return ResponseModel(
                status="Failed", message="Address deletion failed, "
                                         "Address ID might not exist.",
                object={"id": address_id}
            )
    except sqlite3.Error as e:
        return handle_database_error(e)
    except Exception as e:
        return handle_general_error(e)


def get_address(search_inputs: SearchInputs):
    """
    Function to get addresses within a certain distance from
    a given latitude and longitude
    """
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            """SELECT * FROM addresses WHERE
               (latitude - ?) * (latitude - ?) +
               (longitude - ?) * (longitude - ?) <= ? * ?
            """,
            (search_inputs["latitude"], search_inputs["latitude"],
             search_inputs["longitude"], search_inputs["longitude"],
             search_inputs["distance"], search_inputs["distance"])
        )
        addresses = cursor.fetchall()
        connection.close()
        response = []
        if addresses:
            for item in addresses:
                data = {"id": item[0],
                        "address": item[1],
                        "latitude": item[2],
                        "longitude": item[3]}
                response.append(data)
            return response
        return []
    except Exception as e:
        return handle_general_error(e)


def handle_database_error(error):
    """
    Common function to handle database errors
    """
    response_model_error = ResponseModel(
        status="Failed", message=f"Database error occurred: "
                                 f"{str(error)}", object=None
    )
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=response_model_error.dict(),
    )


def handle_general_error(error):
    """
    Common function to handle general errors
    """
    response_model_error = ResponseModel(
        status="Failed", message=f"Exception: {str(error)}", object=None
    )
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=response_model_error.dict()
    )
