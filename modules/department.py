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
        except IntegrityError as e:
            conn.rollback()
            # TASK check other errors
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
            raise DatabaseConnectionError(f"Failed to fetch departments data: {e}")
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

    def update(self, department_id, department_name, department_code):
        conn = DBConnection.get_connection()
        cursor = conn.cursor()

        try:

            fields, values = [], []
            if department_name is not None and department_name != "":
                fields.append("department_name = %s")
                values.append(department_name)
            if department_code is not None and department_code != "":
                fields.append("department_code = %s")
                values.append(department_code)

            if not fields:
                console.print("[INFO] Nothing to update", style="bold orange1")

            # UPDATE departments SET key=val, key2=val2 where deptid = something
            values.append(department_id)
            query = (
                f"UPDATE departments SET {','.join(fields)} WHERE department_id = %s"
            )
            cursor.execute(query, tuple(values))
            conn.commit()
            console.print(f"[OK] Department {department_id} has updated")
        except Error as e:
            raise DatabaseConnectionError(f"Failed to update department: {e}")
        finally:
            DBConnection.close(conn, cursor)

    def delete(self, department_id):
        # "DELETE FROM departments WHERE department_id = %s"
        conn = DBConnection.get_connection()
        cursor = conn.cursor()
        
        try:
            query = "DELETE FROM departments WHERE department_id = %s"
            cursor.execute(query, (department_id,))
            conn.commit()
            console.print(f"[OK] Department with {department_id} has deleted successfully", style="bold orange1")
        except Error as e:
            cursor.rollback()
            raise DatabaseConnectionError(f"Failed to delete department {e}")
        finally:
            DBConnection.close(conn, cursor)
#Test