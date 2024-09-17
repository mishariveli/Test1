import psycopg2
from psycopg2 import sql

# Database connection parameters
conn_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': '123456789',
    'host': '192.168.200.86',  # e.g., 'localhost' or an IP address
    'port': '5432'   # e.g., '5432'
}
name = 'ahmed'
try:
    # Establish a connection to the database
    conn = psycopg2.connect(**conn_params)
    print("Connected to the database")
    # Create a cursor object
    cur = conn.cursor()
    query = f"SELECT id, name, salary FROM employees WHERE name = '{name}';"
    cur.execute(query)
    # Define the query to select id, name, and salary from employees table
    row = cur.fetchone()

    if row:
        print(f"ID: {row[0]}, Name: {row[1]}, Salary: {row[2]}")
    else:
        print(f"No record found with {name}")

except psycopg2.Error as e:
    print(f"An error occurred: {e}")

finally:
    # Close the cursor and connection
    if cur:
        cur.close()
    if conn:
        conn.close()
