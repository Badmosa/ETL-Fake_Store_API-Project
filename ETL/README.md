# Fake Store API ETL Project

A small ETL pipeline that pulls product data from the [Fake Store API](https://fakestoreapi.com), cleans it with pandas, and loads it into a PostgreSQL database.

## 
How it works
Step	| File |	What it does
Extract	Extract.py	Calls the /products and /users endpoints and returns each as a DataFrame
Transform	Transform.py	Renames columns, keeps only the fields needed, converts prices to numeric, and flattens the nested user name and address fields
Load	Load.py	Connects to PostgreSQL with SQLAlchemy and writes each DataFrame to a table
Run	Main.py	Runs the three steps in order
Tech stack

Python · pandas · requests · SQLAlchemy · psycopg2 · python-dotenv ·
