import mysql.connector
from mysql.connector import errorcode

def create_database():
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",      # ✅ Change this if needed
            password="edenyehualashet@123"       # ✅ Enter your actual MySQL password here
        )
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Access denied: Check your username or password")
        else:
            print(f"Error: {err}")
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    create_database()
