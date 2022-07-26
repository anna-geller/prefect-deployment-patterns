"""
brew install postgresql
pip install psycopg2 pandas

def get_db_connection_string() -> str:
    user = "postgres"
    pwd = "postgres"
    return f"postgresql://{user}:{pwd}@localhost:5432/postgres"

def get_df_from_sql_query(table_or_query: str) -> pd.DataFrame:
    db = read_postgres_block()
    engine = create_engine(db)
    return pd.read_sql(table_or_query, engine)

@task
def load_df_to_db(
    df: pd.DataFrame, table_name: str, schema: str = "jaffle_shop"
) -> None:
    conn_string = read_postgres_block()
    db_engine = create_engine(conn_string)
    conn = db_engine.connect()
    conn.execute("CREATE SCHEMA IF NOT EXISTS jaffle_shop;")
    conn.execute(f"DROP TABLE IF EXISTS {schema}.{table_name} CASCADE;")
    df.to_sql(table_name, schema=schema, con=db_engine, index=False)
    conn.close()
"""
from blocks.custom.custom_postgres_block import read_postgres_block
import pandas as pd
from prefect import task, flow, get_run_logger
from sqlalchemy import create_engine
from sqlalchemy.engine import Connection


@task
def load_df_to_db(
    db_conn: Connection,
    df: pd.DataFrame,
    table_name: str,
    schema: str = "jaffle_shop",
) -> None:
    db_conn.execute(f"DROP TABLE IF EXISTS {schema}.{table_name} CASCADE;")
    df.to_sql(table_name, schema=schema, con=db_conn, index=False)


@task
def extract(dataset: str) -> None:
    file = f"https://raw.githubusercontent.com/anna-geller/jaffle_shop/main/data/{dataset}.csv"
    return pd.read_csv(file)


@flow
def extract_and_load():
    logger = get_run_logger()
    conn_string = read_postgres_block()
    db_engine = create_engine(conn_string)
    conn = db_engine.connect()
    conn.execute("CREATE SCHEMA IF NOT EXISTS jaffle_shop;")

    datasets = ["raw_customers", "raw_orders", "raw_payments"]
    for dataset in datasets:
        df = extract(dataset)
        load_df_to_db(conn, df, dataset)
        logger.info("dataset %s loaded", dataset)
    conn.close()  # todo build context manager


if __name__ == "__main__":
    extract_and_load()
