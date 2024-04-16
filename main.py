from fastapi import FastAPI
import uvicorn
import logging
from common.db_connection import create_address_book_table
from routes import address

DESCRIPTION = """
AddressBook API helps you manage addresses. 

## 

You will be able to:

* **Add address**.
* **Read address**.
* **Update address**.
* **Delete address**.
"""

app = FastAPI()

app.include_router(address.router, prefix='/api/address', tags=["APIs for AddressBook"])

try:
    create_address_book_table()
except Exception as ex:  # pylint: disable=W0718
    logging.error("Table initialization failed: %s", ex)


@app.get("/")
async def root():
    """
    Sample API
    :return: ResponseModel
    """
    return {"status": "Success", "message": "Server running..."}


if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
