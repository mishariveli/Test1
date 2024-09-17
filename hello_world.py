# hello_world.py
print("Hello, World! new 92101010")

import psycopg2
from psycopg2 import sql, Error

def fetch_name_salary(name):
    connection = None
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(
            host='192.168.200.86',
            user='postgres',
            password='123456789',
            database='postgres',
            port='5432'
        )

        if connection is not None:
            print("Connected to the database")

            cursor = connection.cursor()

            # Execute query to fetch salary
            query = "SELECT salary FROM name WHERE name = %s"
            cursor.execute(query, (name,))

            result = cursor.fetchone()

            if result:
                print(f"Name {name} salary: {result[0]}")
            else:
                print(f"Name {name} not found")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection is not None:
            cursor.close()
            connection.close()
            print("Database connection closed")

if __name__ == "__main__":
    fetch_name_salary("Ahmed")
