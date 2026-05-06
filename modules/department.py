from mysql.connector import Error, IntegrityError
from db_config import DBConnection
from exceptions.custom_exceptions import DuplicateRecordError, DatabaseConnectionError
from rich.console import Console
from rich.table import Table

console = Console()


class Department:

    def add(self, department_name, department_code):
        conn = DBConnection.get_connection()
        cursor = conn.cursor()

        try:
            query = """
                    INSERT INTO departments(department_name, department_code)
                    VALUES (%s, %s)
                """

            cursor.execute(query, (department_name, department_code))
            conn.commit()
            new_id = cursor.lastrowid
            console.print(
                f"[OK], Department added successfully. ID = {new_id}",
                style="bold green",
            )
            return new_id
        except IndentationError as e:
            conn.rollback()
            raise DuplicateRecordError(
                "Department", "department_code", department_code
            ) from e
        except Error as e:
            conn.rollback()
            raise DatabaseConnectionError(f"Failed to add department: {e}")
        finally:
            DBConnection.close(conn, cursor)

    def get_all(self):
        conn = DBConnection.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM departments")
            return cursor.fetchall()
        except Error as e:
            raise DatabaseConnectionError(f"Failed to fetch departements data: {e}")
        finally:
            DBConnection.close(conn, cursor)

    def get_by_id(self, department_id):
        conn = DBConnection.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            query = "SELECT * FROM departments WHERE department_id = %s"
            cursor.execute(query, (department_id,))
            return cursor.fetchone()
        except Error as e:
            raise DatabaseConnectionError(f"Failed to fetch departments data: {e}")
        finally:
            DBConnection.close(conn, cursor)

    def update(self):
        conn = DBConnection.get_connection()
        cursor = conn.cursor()

    def delete(self):
        pass
