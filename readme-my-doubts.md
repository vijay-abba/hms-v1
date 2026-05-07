

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

answer found but not sure:
because we want a handle in one plase we use multilevel
HMSBaseExpection in safe_run

---


1. 
DBConnection close 
don't we need try and catch blocks while closing 


4. 
in department we can do so it iwll catch or it (currently it is catching in db_confing ? without None )
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

