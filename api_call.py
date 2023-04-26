import requests
import duckdb
import json

url = 'https://api.exchangerate.host/2023-04-04'
response = requests.get(url)
data = response.json()

with open("data.json", "w") as f:
    json.dump(data, f)


con = duckdb.connect(database='targetapidatabase.db')


query = "CREATE TABLE exchangerate AS SELECT * FROM read_json_auto('data.json')"
con.execute(query)


result = con.execute("SELECT rates.MAD FROM exchangerate ").fetchall()
print(result)
