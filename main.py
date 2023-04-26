import duckdb
import requests

# CSV FILE

# specify the file paths
csv_file = "customer_shopping_data.csv.csv"
db_file = "mydatabase.db"

# create a DuckDB connection
conn = duckdb.connect(db_file)


'''
create a table in DuckDB from the CSV file : 

THIS STEP IS DONE ONCE

'''
#query = f"CREATE TABLE customer_shopping_data AS SELECT * FROM read_csv_auto('{csv_file}')"
#conn.execute(query)


# query the data in the table
#result = conn.execute("SELECT * FROM customer_shopping_data.csv LIMIT 4").fetchall()

# Let's do some querying

insert_into = conn.execute("INSERT INTO customer_shopping_data.csv VALUES ('oumaima', 'cat1' , 'cat11' , 'https://m.media.jpg', 'link.com' , 2 , 4 , 33 , 44 )")
#select last row
select_last = conn.execute("SELECT * FROM customer_shopping_data.csv ORDER BY name DESC LIMIT 1;")
#select

# print the result
print(insert_into)
print(select_last)


