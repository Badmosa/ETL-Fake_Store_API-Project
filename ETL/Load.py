from sqlalchemy import create_engine

host = 'localhost'
port = 0000
user = 'postgres'
password = 'input password'
db_name = 'fake_store_db'

def load_to_postgress(df, table_name):
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')

    df.to_sql(
        table_name,
        engine,
        if_exists = 'replace',
        index = False
    )

print('data loaded to postgres successfully')