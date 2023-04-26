import duckdb
import requests

# CSV FILE

# specify the file paths
csv_file = "customer_shopping_data.csv"
db_file = "mydatabase.db"

# create a DuckDB connection
conn = duckdb.connect(db_file)


query = f"CREATE TABLE if not exists customer_shopping_data AS SELECT * FROM read_csv_auto('{csv_file}')"
conn.execute(query)


# query the data in the table
result = conn.execute("SELECT * FROM customer_shopping_data LIMIT 4").fetchall()
print(result)


