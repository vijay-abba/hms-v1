`pip3 install rich`

`pip3 install mysql-connector-python`

### Python String Formatting vs. Database Parameterization

- **String Formatting**: `%s` in strings (e.g., `"Name: %s" % name`) uses Python's `%` operator to replace placeholders with values from a tuple. Pure string manipulation.

- **Database Queries**: `%s` in SQL (e.g., `cursor.execute(query, params)`) are placeholders handled by the database library (like `mysql-connector`). The tuple provides safe parameter substitution—no Python `%` operator involved. Prevents SQL injection.

Parameterized queries with `%s` placeholders prevent SQL injection because the database driver (e.g., `mysql-connector`) treats the values in the tuple `(department_name, department_code)` as literal data, not executable SQL code. Even if a malicious user inputs SQL-like strings (e.g., `department_name = "'; DROP TABLE departments; --"`), they are escaped and inserted as plain text, not executed.

This is why `cursor.execute(query, params)` is safe, unlike unsafe string concatenation (e.g., `query = f"INSERT ... VALUES ({user_input})"`), which could allow injection. Always use parameterized queries for user inputs. If you have more questions about security, let me know.

---

### Database Connection and Cursor Explanation

In database programming with MySQL (using `mysql-connector-python`), `conn` and `cursor` are key objects for interacting with the database safely and efficiently.

#### Connection (`conn`)
- **What it is**: A `Connection` object represents an active link to the MySQL database server. It's like opening a phone line to the database—you need it to send and receive data.
- **Purpose**: Manages the session with the database, including authentication, transaction handling, and ensuring data integrity. Without a connection, you can't do anything with the database.
- **Lifecycle**: Created when you connect (e.g., via `mysql.connector.connect()`), used for the session, and must be closed to free resources and avoid leaks.

#### Cursor (`cursor`)
- **What it is**: A `Cursor` object is a tool (or "pointer") created from a connection. It executes SQL queries and fetches results.
- **Purpose**: Allows you to run SQL commands (e.g., SELECT, INSERT) on the connection. Think of it as the "worker" that sends queries to the database and retrieves responses. Cursors can be configured for different behaviors (e.g., returning results as dictionaries).
- **Lifecycle**: Created from a connection (e.g., `conn.cursor()`), used for queries, and closed after use to release resources.

#### What `get_connection()` Does
- **Exact steps**:
  1. Uses `mysql.connector.connect(**DB_CONFIG)` to create a new `Connection` object (`conn`) with the provided config (host, user, password, database).
  2. Checks if the connection is active with `conn.is_connected()`.
  3. If connected, prints a success message and returns the `conn` object for use elsewhere.
  4. If not connected or an error occurs (e.g., wrong credentials), raises a `DatabaseConnectionError`.
- **Why?** This method centralizes connection creation, ensuring consistent setup and error handling. It returns a ready-to-use connection.

#### What `close()` Does
- **Exact steps**:
  1. If a `cursor` is provided, calls `cursor.close()` to release the cursor's resources (e.g., any pending results).
  2. If `conn` is provided and still connected (`conn.is_connected()`), calls `conn.close()` to end the database session and free the connection.
  3. Prints confirmation messages for each close operation.
- **Why?** Databases have limited connections; not closing them can lead to resource exhaustion or locks. This method ensures proper cleanup, typically called in a `finally` block or with context managers.

#### Usage Pattern in Your Code
- Get a connection: `conn = DBConnection.get_connection()`
- Create a cursor: `cursor = conn.cursor(dictionary=True)` (for dict results)
- Execute queries: `cursor.execute(query, params)`
- Fetch results: `cursor.fetchall()` or `cursor.fetchone()`
- Close resources: `DBConnection.close(conn, cursor)` (in `finally`)

This setup promotes best practices: parameterized queries for security, proper resource management, and error handling. If you have specific code examples or more questions, provide details.


---


