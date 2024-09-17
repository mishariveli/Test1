print("Hello, World! new 92101010")

import psycopg2
from psycopg2 import Error

name = 'ahmed'
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
            query = "SELECT salary FROM employees WHERE name = '{name}'"
            cursor.execute(query)

            result = cursor.fetchone()

            if result:
                print(f"Salary for {name}: {result[0]}")
            else:
                print(f"{name} not found")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection is not None:
            cursor.close()
            connection.close()
            print("Database connection closed")
