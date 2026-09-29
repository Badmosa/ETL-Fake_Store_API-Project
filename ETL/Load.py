import os
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

url = URL.create(
    drivername='postgresql',
    username='postgres',
    password=os.getenv('Badmosbasa66'),
    host='localhost',
    port=5432,
    database='fake_store_db',
)
engine = create_engine(url)

def load_to_postgres(df, table_name):
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f'{table_name} loaded to postgres successfully')