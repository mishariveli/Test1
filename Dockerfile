# Use a base image with Python installed
FROM python:3.11-slim

# Install necessary packages
RUN apt-get update && \
    apt-get install -y python3-pip

# Install Python packages
RUN pip install psycopg2-binary

# Copy your application code
COPY hello_world.py /app/hello_world.py

# Set the working directory
WORKDIR /app

# Command to run the Python script
CMD ["python3", "hello_world.py"]
