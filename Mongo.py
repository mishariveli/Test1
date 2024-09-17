from pymongo import MongoClient

# MongoDB connection parameters
conn_params = {
    'host': 'mongodb://192.168.200.86:27017/',  # MongoDB URI
    'database': 'creative',  # Name of your MongoDB database
    'collection': 'employees'  # Name of your MongoDB collection
}

first_name = 'John'

try:
    # Establish a connection to the MongoDB database
    client = MongoClient(conn_params['host'])
    print("Connected to the database")

    # Access the database and collection
    db = client[conn_params['database']]
    collection = db[conn_params['collection']]

    # Define the query to find the document with the specified name
    query = {"name": name}
    document = collection.find_one(query)

    if document:
        # Print the ID, name, and salary of the document
        print(f"ID: {document.get('_id')}, Name: {document.get('name')}, Salary: {document.get('salary')}")
    else:
        print(f"No record found with {name}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the connection
    client.close()
