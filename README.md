# Address Management Application

## Overview

This FastAPI application provides APIs for managing addresses. It allows users to add, update, retrieve, and delete addresses from a database.

## Features

- Add a new address
- Update an existing address
- Retrieve addresses based on search criteria
- Delete an address

## Technologies Used

- FastAPI: FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.11.
- SQLite: SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.
- Python: The backend logic of this application is written in Python.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/DeepthiVDevanandan/address_book.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
   This command starts the FastAPI server locally. The `--reload` flag enables automatic reloading of the server when code changes are detected.

## API Documentation

- Swagger UI: Access the API documentation and test endpoints using Swagger UI. Open a web browser and navigate to `http://localhost:8000/docs`.

## API Endpoints

- `POST /address/`: Add a new address to the database.
- `GET /address/`: Retrieve addresses from the database based on search criteria.
- `PATCH /address/`: Update an existing address in the database.
- `DELETE /address/{address_id}/`: Delete an address from the database.
