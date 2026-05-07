from rich.console import Console
import mysql.connector
from mysql.connector import Error
from exceptions.custom_exceptions import DatabaseConnectionError

console = Console()

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "vijay@123",
    "database": "hms",
}


class DBConnection:

    @staticmethod
    def get_connection():
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            if conn.is_connected():
                console.print("Connected to Database Successfully ", style="bold green")
                return conn
            raise DatabaseConnectionError(
                "Connection Object is created but not connected"
            )
        except Error as e:
            raise DatabaseConnectionError(f"MySQL error: {e}")

    @staticmethod
    def close(conn, cursor=None):
        if cursor:
            cursor.close()
            console.print("Connection closed for cursor", style="bold orange1")
        if conn and conn.is_connected():
            conn.close()
            console.print("Connection closed for conn", style="bold orange1")


# conn = DBConnection.get_connection()
# print(conn)
# DBConnection.close(conn)
