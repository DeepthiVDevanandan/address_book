from datetime import datetime
import sqlite3
from fastapi import status
from fastapi.responses import JSONResponse
from common.db_connection import create_connection
from model.response_model import ResponseModel
from model.add_address_model import AddAddress
from model.get_address_model import SearchInputs
from model.update_address_model import UpdateAddress


# Function to save an address to the database
def save_address(address: AddAddress):
    try:
        created_date = datetime.now()
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO addresses (address, latitude, longitude, created_on) VALUES (?,?,?,?)",
            (address.address, address.latitude, address.longitude, created_date))  # Fix: Changed latitude to longitude
        address_id = cursor.lastrowid
        connection.commit()
        connection.close()
        if address_id > 0:  # Fix: Corrected the condition to check if address_id is greater than 0
            return ResponseModel(
                status="Success", message=f"Address saved successfully", object={"id": address_id}
            )
    except sqlite3.Error as e:
        return handle_database_error(e)
    except Exception as e:
        return handle_general_error(e)


# Function to update an existing address in the database
def update_address(address: UpdateAddress):
    try:
        updated_on = datetime.now()
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            """ UPDATE addresses SET address = ?, latitude = ?, longitude = ?, updated_on = ?
            WHERE id = ?""",
            (address.address, address.latitude, address.longitude, address.id, updated_on))  # Fix: Changed latitude to longitude
        rows_updated = cursor.rowcount
        connection.commit()
        connection.close()
        if rows_updated > 0:
            return ResponseModel(
                status="Success", message=f"Address updated successfully", object={"id": address.id}
                # Fix: Corrected message for successful update
            )
        else:
            return ResponseModel(
                status="Failed", message=f"Address update failed, Address ID might not exist.",
                object={"id": address.id}  # Fix: Corrected message for failed update
            )
    except sqlite3.Error as e:
        return handle_database_error(e)
    except Exception as e:
        return handle_general_error(e)


# Function to delete an address from the database
def delete_address(address_id):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
                DELETE FROM addresses
                WHERE id = ?
            """
            ,
            (address_id,))
        rows_affected = cursor.rowcount  # Fix: Get row count after execution
        connection.commit()
        connection.close()
        if rows_affected > 0:
            return ResponseModel(
                status="Success", message=f"Address deleted successfully", object={"id": address_id}
                # Fix: Corrected message for successful deletion
            )
        else:
            return ResponseModel(
                status="Failed", message=f"Address deletion failed, Address ID might not exist.",
                object={"id": address_id}  # Fix: Corrected message for failed deletion
            )
    except sqlite3.Error as e:
        return handle_database_error(e)
    except Exception as e:
        return handle_general_error(e)


# Function to get addresses within a certain distance from a given latitude and longitude
def get_address(search_inputs: SearchInputs):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            """SELECT * FROM addresses WHERE 
               (latitude - ?) * (latitude - ?) + 
               (longitude - ?) * (longitude - ?) <= ? * ?
            """,
            (search_inputs["latitude"], search_inputs["latitude"], search_inputs["longitude"],
             search_inputs["longitude"], search_inputs["distance"], search_inputs["distance"])
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
        else:
            return []
    except Exception as e:
        return handle_general_error(e)


# Common function to handle database errors
def handle_database_error(error):
    response_model_error = ResponseModel(
        status="Failed", message=f"Database error occurred: {str(error)}", object=None
    )
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=response_model_error.dict(),
    )


# Common function to handle general errors
def handle_general_error(error):
    response_model_error = ResponseModel(
        status="Failed", message=f"Exception: {str(error)}", object=None
    )
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=response_model_error.dict()
    )
