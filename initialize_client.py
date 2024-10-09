from influxdb_client_3 import InfluxDBClient3, Point
import time

# Your API token, organization, and host details
token = "iwv2CWqnBVUJs_V858FM8VxBeVBw7njvcM9VKzadq-43FITws8la97gAni3L2lDwAH0DxiClTSH2yhtZ6BkCsA=="
org = "Database"
host = "https://us-east-1-1.aws.cloud2.influxdata.com"

# Initialize the client
client = InfluxDBClient3(host=host, token=token, org=org)

# Specify your bucket name
database = "TestBucket"

# Updated data points with angles
data = {
    "point1": {"angle": 30},
    "point2": {"angle": 60},
    "point3": {"angle": 90},
    "point4": {"angle": 120},
    "point5": {"angle": 150},
}

# Write points to your bucket
for key in data:
    point = (
        Point("angles")
        .field("angle", data[key]["angle"])
    )
    client.write(database=database, record=point)
    print(f"Written angle {data[key]['angle']} to database.")
    time.sleep(2)  # separate points by 2 seconds

print("Complete. Return to the InfluxDB UI.")
