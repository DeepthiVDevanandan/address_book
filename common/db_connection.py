
import sqlite3


def create_connection():
    connection = sqlite3.connect("Test.db")
    return connection


def create_address_book_table():
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
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        drop TABLE  addresses
    """)
    connection.commit()
    connection.close()
