from mysql.connector import Error, IntegrityError
from db_config import DBConnection
from exceptions.custom_exceptions import DuplicateRecordError, DatabaseConnectionError
from rich.console import Console
from rich.table import Table

console = Console()


class Patient:

    def add(self, patient_data):
        patient_name = patient_data.get("patient_name")
        age = patient_data.get("age")
        gender = patient_data.get("gender")
        phone_number = patient_data.get("phone_number")
        address = patient_data.get("address")

        conn = DBConnection.get_connection()
        cursor = conn.cursor()

        try:
            query = """
                    INSERT INTO patients(patient_name, age,gender, phone_number,address)
                    VALUES (%s, %s, %s, %s, %s)
                """

            cursor.execute(query, (patient_name, age, gender, phone_number, address))
            conn.commit()
            new_id = cursor.lastrowid
            console.print(
                f"[OK], Patients added successfully. ID = {new_id}",
                style="bold green",
            )
            return new_id
        except IntegrityError as e:
            conn.rollback()
            # TASK check other errors
            raise DuplicateRecordError("Patient", "phone_number", phone_number) from e
        except Error as e:
            conn.rollback()
            raise DatabaseConnectionError(f"Failed to add patient: {e}")
        finally:
            DBConnection.close(conn, cursor)

    def get_all(self):
        conn = DBConnection.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM patients")
            return cursor.fetchall()
        except Error as e:
            raise DatabaseConnectionError(f"Failed to fetch patients data: {e}")
        finally:
            DBConnection.close(conn, cursor)

    def get_by_id(self, patient_id):
        conn = DBConnection.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            query = "SELECT * FROM patients WHERE patient_id = %s"
            cursor.execute(query, (patient_id,))
            return cursor.fetchone()
        except Error as e:
            raise DatabaseConnectionError(f"Failed to fetch patients data: {e}")
        finally:
            DBConnection.close(conn, cursor)

    def update(self,patient_data):
        patient_id = patient_data.get("patient_id")
        patient_name = patient_data.get("patient_name")
        age = patient_data.get("age")
        gender = patient_data.get("gender")
        phone_number = patient_data.get("phone_number")
        address = patient_data.get("address")


        conn = DBConnection.get_connection()
        cursor = conn.cursor()

        try:

            fields, values = [], []
            if patient_name is not None and patient_name != "":
                fields.append("patient_name = %s")
                values.append(patient_name)
            if age is not None and age != "":
                fields.append("age = %s")
                values.append(age)
            if gender is not None and gender != "":
                fields.append("gender = %s")
                values.append(gender)
            if phone_number is not None and phone_number != "":
                fields.append("phone_number = %s")
                values.append(phone_number)
            if address is not None and address != "":
                fields.append("address = %s")
                values.append(address)
            

            if not fields:
                console.print("[INFO] Nothing to update", style="bold orange1")

            values.append(patient_id)
            query = (
                f"UPDATE patients SET {','.join(fields)} WHERE patient_id = %s"
            )
            cursor.execute(query, tuple(values))
            conn.commit()
            console.print(f"[OK] patient {patient_id} has updated")
        except Error as e:
            raise DatabaseConnectionError(f"Failed to update patients: {e}")
        finally:
            DBConnection.close(conn, cursor)

    def delete(self, patient_id):
        conn = DBConnection.get_connection()
        cursor = conn.cursor()

        try:
            query = "DELETE FROM patients WHERE patient_id = %s"
            cursor.execute(query, (patient_id,))
            conn.commit()
            console.print(
                f"[OK] Patient with {patient_id} has deleted successfully",
                style="bold orange1",
            )
        except Error as e:
            cursor.rollback()
            raise DatabaseConnectionError(f"Failed to delete Patient {e}")
        finally:
            DBConnection.close(conn, cursor)


# Test
