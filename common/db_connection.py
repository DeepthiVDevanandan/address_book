"""
database connection module
"""
import sqlite3


def create_connection():
    """
    Create a connection to the SQLite database.

    Returns:
        sqlite3.Connection: A connection object to the SQLite database.
    """
    connection = sqlite3.connect("Test.db")
    return connection


def create_address_book_table():
    """
    Create the addresses table in the database if it doesn't exist.
    """
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS addresses
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            address TEXT NOT NULL,
            latitude FLOAT NOT NULL,
            longitude FLOAT NOT NULL,
            created_on DATE NULL,
            updated_on DATE NULL
        )
    """)
    connection.commit()
    connection.close()


def drop_address_book_table():
    """
    Drop the addresses table from the database.
    """
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS addresses
    """)
    connection.commit()
    connection.close()
