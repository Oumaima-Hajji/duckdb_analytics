import requests
import duckdb
import json
import pandas as pd

api_key = "YOUR API KEY HERE"
url = f"https://api.nasa.gov/insight_weather/?api_key={api_key}&feedtype=json&ver=1.0"

response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the JSON data from the response
    data = response.json()

    # Do something with the data, for example print it
    print(data.keys())
    

# Convert JSON dictionary to a string
json_string = json.dumps(data)

# Load JSON string into a Pandas dataframe
df = pd.json_normalize(json.loads(json_string))


#print(df.head(4))
# Connect to the DuckDB database
con = duckdb.connect(database='APIdatabase.db')
# Load dataframe into a DuckDB table
con.register('mars_weather', df)

# Query the table
result = con.execute("SELECT * FROM mars_weather").fetchall()
print(result)

