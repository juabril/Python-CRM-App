#Install MySQL on computer
#https://dev.mysql.com/downloads/installer/
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python
# JAA Note: This file was upgraded using GitHub Copilot to handle the error


import mysql.connector
from mysql.connector import Error
import os

dataBase = None
cursorObject = None

try:
    # Use environment variables for sensitive data
    conn_kwargs = {
        'host': os.getenv('DB_HOST', 'localhost'),
        'user': os.getenv('DB_USER', 'root'),
        'passwd': os.getenv('DB_PASSWORD', 'oH9qKSBd7YaK')
    }

    # Optional: if you need to force an auth plugin, set DB_AUTH_PLUGIN env var
    auth_plugin = os.getenv('DB_AUTH_PLUGIN')
    if auth_plugin:
        conn_kwargs['auth_plugin'] = auth_plugin

    dataBase = mysql.connector.connect(**conn_kwargs)

    # Prepare a cursor object
    cursorObject = dataBase.cursor()

    # Create a database only if it doesn't exist
    cursorObject.execute("CREATE DATABASE IF NOT EXISTS goldenrecord")

    print("Database setup completed successfully!")

except Error as e:
    msg = str(e)
    print(f"Error while connecting to MySQL: {msg}")
    # Common cause: MySQL 8+ uses caching_sha2_password by default.
    if 'caching_sha2_password' in msg:
        print("Possible fixes:\n - Upgrade the Python MySQL driver: `pip install -U mysql-connector-python`\n - Or set the MySQL user to use mysql_native_password on the server:\n   `ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '<password>';`\n - Or set env var DB_AUTH_PLUGIN=caching_sha2_password if your driver supports it.")

finally:
    # Close the cursor and connection if they were created
    try:
        if cursorObject:
            cursorObject.close()
    except Exception:
        pass
    try:
        if dataBase and getattr(dataBase, 'is_connected', lambda: True)():
            dataBase.close()
    except Exception:
        pass


"""
import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'oH9qKSBd7YaK', 

)

# prepare a cursor object
cursorObject = dataBase.cursor()

#Create a database
cursorObject.execute("CREATE DATABASE goldenrecord")

print("All done!")
"""
