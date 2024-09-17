from pymongo import MongoClient

# MongoDB connection parameters
conn_params = {
    'host': 'mongodb://192.168.200.86:27017/',  # MongoDB URI
    'database': 'creative',  # Name of your MongoDB database
    'collection': 'employees'  # Name of your MongoDB collection
        'collection': 'employees'  # Name of your MongoDB collection
}

# Define the first name
first_name = 'Khaled'

try:
    # Establish a connection to the MongoDB database
    client = MongoClient(conn_params['host'])
    print("Connected to the database")

    # Access the database and collection
    db = client[conn_params['database']]
    collection = db[conn_params['collection']]

    # Define the query to find the document with the specified first name
    query = {"first_name": first_name}
    document = collection.find_one(query)

    if document:
        # Print the ID, first name, and salary of the document
        print(f"ID: {document.get('_id')}, First Name: {document.get('first_name')}, Salary: {document.get('salary')}")
    else:
        print(f"No record found with First Name: {first_name}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the connection
    client.close()
