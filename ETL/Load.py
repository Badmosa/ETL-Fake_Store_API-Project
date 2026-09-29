import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

load_dotenv(Path(__file__).resolve().parent.parent / '.env')

url = URL.create(
    drivername='postgresql+psycopg2',
    username='postgres',
    password=os.getenv('PG_PASSWORD'),
    host='localhost',
    port=2665,
    database='fake_store_db',
)
engine = create_engine(url)

def load_to_postgres(df, table_name):
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f'{table_name} loaded to postgres successfully')