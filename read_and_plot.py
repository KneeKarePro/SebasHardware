from influxdb_client_3 import InfluxDBClient3
import pandas as pd
import matplotlib.pyplot as plt

# Your API token, organization, and host details
token = "iwv2CWqnBVUJs_V858FM8VxBeVBw7njvcM9VKzadq-43FITws8la97gAni3L2lDwAH0DxiClTSH2yhtZ6BkCsA=="
org = "Database"
host = "https://us-east-1-1.aws.cloud2.influxdata.com"

# Initialize the client
client = InfluxDBClient3(host=host, token=token, org=org)

# Specify your bucket name
bucket_name = "TestBucket"

# SQL query to execute
query = """
SELECT *
FROM 'angles'
WHERE time >= now() - interval '24 hours'
AND angle IS NOT NULL
"""

# Execute the query
table = client.query(query=query, database=bucket_name, language='sql')

# Convert the result to a pandas DataFrame
df = table.to_pandas().sort_values(by="time")

# Print the DataFrame
print(df)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(df['time'], df['angle'], marker='o', linestyle='-', color='b')
plt.title("Angles over Time")
plt.xlabel("Time")
plt.ylabel("Angle (degrees)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Optionally, save the DataFrame to a CSV file
# df.to_csv("influxdb_angle_data.csv", index=False)
