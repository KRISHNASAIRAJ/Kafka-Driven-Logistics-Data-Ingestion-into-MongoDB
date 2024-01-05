import pandas as pd
from confluent_kafka import SerializingProducer
from confluent_kafka.schema_registry.avro import AvroSerializer
from confluent_kafka.serialization import StringSerializer
from confluent_kafka.schema_registry import SchemaRegistryClient


def delivery_report(
    err, msg
):  # It reports the delivery status of the data to kafka cluster
    if err is not None:  # If some error is found
        print("Delivery failed for User record {}: {}".format(msg.key(), err))
        return
    print(
        "User record successfully produced to {} [{}] at offset {}".format(
            msg.topic(), msg.partition(), msg.offset()
        )  # If message was successfully sent to cluster
    )


kafka_config = {
    "bootstrap.servers": "************",  # The host url of kafka server(cloud)
    "sasl.mechanisms": "PLAIN",  # SASL mechanisms for authentication
    "security.protocol": "SASL_SSL",  # Security Protocol
    "sasl.username": "***********",  # SASL USERNAME(API)
    "sasl.password": "****************************",  # SASL PASSWORD(API)
}
# Create a Schema Registry client which manages the updated schema
schema_registry_client = SchemaRegistryClient(
    {
        "url": "***********",  # The host url of schema registry
        "basic.auth.user.info": "{}:{}".format(
            "*************",  # Schema Registry API key
            "**********************************",  # Schema registry API value/secret
        ),
    }
)

# Fetch the latest Avro schema for the value
subject_name = "truck_data-value"  # topic_name+(-value)
schema_str = schema_registry_client.get_latest_version(
    subject_name
).schema.schema_str  # It gives the latest updated schema version as string(actual one in ui)

# Create Avro Serializer for the value
key_serializer = StringSerializer("utf_8")  # Serializer for keys, encoded as strings
avro_serializer = AvroSerializer(
    schema_registry_client, schema_str
)  # Serializer for Avro schema

# Define the SerializingProducer object which publishes data
producer = SerializingProducer(
    {
        "bootstrap.servers": kafka_config["bootstrap.servers"],  # Kafka host server url
        "security.protocol": kafka_config[
            "security.protocol"
        ],  # Security protocol configuration
        "sasl.mechanisms": kafka_config[
            "sasl.mechanisms"
        ],  # SASL mechanisms for authentication
        "sasl.username": kafka_config["sasl.username"],  # SASL USERNAME(API)
        "sasl.password": kafka_config["sasl.password"],  # SASL PASSWORD(API)
        "key.serializer": key_serializer,  # Key will be serialized as a string
        "value.serializer": avro_serializer,  # Value will be serialized as Avro
    }
)
df = pd.read_csv("delivery_trip_truck_data.csv")#Read csv file as df
df.fillna("null")#Fill null values

for index, row in df.iterrows():
    logistics_data = {
        "GpsProvider": str(row["GpsProvider"]),
        "BookingID": str(row["BookingID"]),
        "Market/Regular ": str(row["Market/Regular "]),
        "BookingID_Date": str(row["BookingID_Date"]),
        "vehicle_no": str(row["vehicle_no"]),
        "Origin_Location": str(row["Origin_Location"]),
        "Destination_Location": str(row["Destination_Location"]),
        "Org_lat_lon": str(row["Org_lat_lon"]),
        "Des_lat_lon": str(row["Des_lat_lon"]),
        "Data_Ping_time": str(row["Data_Ping_time"]),
        "Planned_ETA": str(row["Planned_ETA"]),
        "Current_Location": str(row["Current_Location"]),
        "DestinationLocation": str(row["DestinationLocation"]),
        "actual_eta": str(row["actual_eta"]),
        "Curr_lat": str(row["Curr_lat"]),
        "Curr_lon": str(row["Curr_lon"]),
        "ontime": str(row["ontime"]),
        "delay": str(row["delay"]),
        "OriginLocation_Code": str(row["OriginLocation_Code"]),
        "DestinationLocation_Code": str(row["DestinationLocation_Code"]),
        "trip_start_date": str(row["trip_start_date"]),
        "trip_end_date": str(row["trip_end_date"]),
        "TRANSPORTATION_DISTANCE_IN_KM": (row["TRANSPORTATION_DISTANCE_IN_KM"]),
        "vehicleType": str(row["vehicleType"]),
        "Minimum_kms_to_be_covered_in_a_day": str(
            row["Minimum_kms_to_be_covered_in_a_day"]
        ),
        "Driver_Name": str(row["Driver_Name"]),
        "Driver_MobileNo": str(row["Driver_MobileNo"]),
        "customerID": str(row["customerID"]),
        "customerNameCode": str(row["customerNameCode"]),
        "supplierID": str(row["supplierID"]),
        "supplierNameCode": str(row["supplierNameCode"]),
        "Material Shipped": str(row["Material Shipped"]),
    }

    producer.produce(
        topic="truck_data",
        key=str(row["BookingID"]),
        value=logistics_data,
        on_delivery=delivery_report,
    )# Push the record into the specified topic with the given key-value pair
    producer.flush()# Flush the producer buffer to ensure all messages are sent
    print(index)#Printing the doc index
print("All Data successfully published to Kafka")
