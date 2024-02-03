# Kafka-Driven-Logistics-Data-Ingestion-into-MongoDB
The project orchestrates a pipeline to process logistics data using Kafka messaging and stores it efficiently in MongoDB. It involves Kafka producer and consumer scripts, Docker for scalability, and integrates Avro schema for data serialization.


## Features
* Kafka Integration: Utilizes Kafka messaging for handling logistics data.
* Scalable Consumers: Docker scaling to manage the processing load with a consumer group of 3 instances.
* Data Serialization: Implements Avro schema represented in avro.json for data serialization.
* File Included: Contains delivery_trip_truck_data.csv for data ingestion.
* Kafka Topic Creation: A Kafka topic named 'truck_data' created with 10 partitions.


## Technology Used
* Python Scripts:
    * kafka_producer.py: Sends logistics data to Kafka.
    * kafka_consumer.py: Processes data from Kafka and stores it in MongoDB.It starts consuming the earliest message available in the partition.
* Docker: Utilized to scale consumer instances using the docker-compose.yml file.
* Data Schema: Avro schema represented in avro.json for structured data handling.
* File Contents: delivery_trip_truck_data.csv: Contains logistics data for ingestion.
* Kafka Configuration:
    * Kafka topic: 'truck_data' created with 10 partitions.
* MongoDB:Database for storing the logistics data
 

## How to Use
* Setting Up Kafka: Ensure 'truck_data' Kafka topic is created with 10 partitions.
* Running the Pipeline:
    * Execute kafka_producer.py to send logistics data to Kafka.
    * Use Docker to scale consumer instances (docker-compose up --scale co=3).
* Avro Schema Integration: Refer to avro.json for the Avro schema utilized in Kafka topic creation.
* File Usage: delivery_trip_truck_data.csv: Contains logistics data for ingestion.

## Producer &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Consumer
<div style="display:flex; justify-content: center;">
  <img width="398" alt="Screenshot 2024-01-04 235750" src="https://github.com/KRISHNASAIRAJ/Kafka-Driven-Logistics-Data-Ingestion-into-MongoDB-with-Python/assets/90061814/a60f8e69-944d-43a1-957c-faf41dfdd03e">
<img width="315" alt="Screenshot 2024-01-05 125504" src="https://github.com/KRISHNASAIRAJ/Kafka-Driven-Logistics-Data-Ingestion-into-MongoDB-with-Python/assets/90061814/843090d3-da47-45fa-ad48-1035b9d02b03">

</div>

## MongoDB Database &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; MongoDB Collection
<div style="display:flex; justify-content: center;">
  <img width="398" alt="Screenshot 2024-01-05 141253" src="https://github.com/KRISHNASAIRAJ/Kafka-Driven-Logistics-Data-Ingestion-into-MongoDB-with-Python/assets/90061814/abab486e-3ee1-44d3-98ff-a047ceab7f01">
<img width="380" alt="Screenshot 2024-01-05 140926" src="https://github.com/KRISHNASAIRAJ/Kafka-Driven-Logistics-Data-Ingestion-into-MongoDB-with-Python/assets/90061814/f8477175-2606-4c9c-b6ba-6cb390a6655f">


</div>
