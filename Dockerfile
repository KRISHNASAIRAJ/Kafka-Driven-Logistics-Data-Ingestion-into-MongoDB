# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies your consumer script might need
RUN pip install --no-cache-dir confluent-kafka pymongo requests fastavro

# Run your script when the container launches
CMD ["python", "kafka_consumer.py"]
