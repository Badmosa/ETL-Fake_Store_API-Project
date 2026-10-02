# Fake Store API ETL Pipeline

A simple ETL pipeline that pulls product and user data from the [Fake Store API](https://fakestoreapi.com), cleans it with pandas, and loads it into a PostgreSQL database.

## How it works

| Step | File | What it does |
|------|------|--------------|
| **Extract** | `Extract.py` | Calls the `/products` and `/users` endpoints and returns each as a DataFrame |
| **Transform** | `Transform.py` | Renames columns, keeps only the fields needed, converts prices to numeric, and flattens the nested user `name` and `address` fields |
| **Load** | `Load.py` | Connects to PostgreSQL with SQLAlchemy and writes each DataFrame to a table |
| **Run** | `Main.py` | Runs the three steps in order |

## Tech stack

Python · pandas · requests · SQLAlchemy · psycopg2 · python-dotenv · PostgreSQL

## Output

Two tables in the `fake_store_db` database:

**`products`**: `product_id`, `product_name`, `product_price`, `product_category`, `product_description`

**`users`**: `user_id`, `user_email`, `username`, `first_name`, `last_name`, `street`, `city`, `zipcode`

Tables are replaced on every run, so re-running the pipeline never creates duplicates.

## Getting started

**1. Clone the repo**

```bash
git clone https://github.com/Badmosa/ETL-Fake_Store_API-Project.git
cd ETL-Fake_Store_API-Project
```

**2. Install dependencies**

```bash
pip install pandas requests sqlalchemy psycopg2-binary python-dotenv
```

**3. Create the database**

Create an empty PostgreSQL database named `fake_store_db`.

**4. Add your password**

Create a `.env` file one folder above `Load.py` (the parent directory) containing:

```
PG_PASSWORD=your_postgres_password
```

**5. Check the connection settings**

In `Load.py`, the defaults are user `postgres`, host `localhost`, port `2665`. Change the port to `5432` (the PostgreSQL default) or whatever your setup uses.

**6. Run it**

```bash
python Main.py
```

You should see progress messages for each stage, ending with `ETL pipeline completed`.

## Project structure

```
├── Extract.py
├── Transform.py
├── Load.py
└── Main.py
```

## Possible improvements

- Add the `/carts` endpoint
- Add logging and error handling around the load step
- Schedule runs with cron or Airflow
- Build a Power BI dashboard on top of the Postgres tables

## Author

**Badmos Ayomide**, Data Engineer
[LinkedIn](https://linkedin.com/in/badmosayomide)