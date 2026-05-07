

IntegrityError
1. In `expect IntegrityError` block  we are giving raising `DuplicateRecordError`  but IntegrityError could be other error's also right.


---

2. Why we are using MultiLevel Inheritance 
class HMSBaseExpection(Exception):
class DatabaseConnectionError(HMSBaseExpection):
class DuplicateRecordError(DatabaseConnectionError):

WE CAN use this 
class HMSBaseExpection(Exception):
class DatabaseConnectionError(Exception):
class DuplicateRecordError(Exception):

similar answer:
because we want a handle in one plase we use multilevel
HMSBaseExpection in safe_run

---


3. 
DBConnection close 
don't we need try and catch blocks while closing 


4. 
in department 
cursor = None
conn = None
and inside try 
try {
    conn = DBConnection.get_connection()
    cursor = conn.cursor()
}

---
5. 
General exception is only in safe_run why we don't have in other try expect blocks 
except Exception as e:

