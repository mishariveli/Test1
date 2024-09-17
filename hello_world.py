# hello_world.py
print("Hello, World! new 92101010")
import psycopg2
from psycopg2 import sql, Error

def fetch_user_salary(username):
    try:
        connection = mysql.connector.connect(
            host='192.168.200.86',
            user='postgre',
            password='123456789',
            database='postgre',
            port='5432'
        )

        if connection.is_connected():
            print("Connected to the database")

            cursor = connection.cursor()

        
            query = "SELECT salary FROM users WHERE username = %s"
            cursor.execute(query, (username,))
          
            result = cursor.fetchone()

            if result:
                print(f"User {username} salary: {result[0]}")
            else:
                print(f"User {username} not found")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Database connection closed")

if __name__ == "__main__":
   
    fetch_user_salary("Ahmed")
