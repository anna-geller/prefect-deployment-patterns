"""
prefect deployment build -n prod -q prod -a flows/ingestion.py:ingestion
prefect deployment build -n prod -q prod -a flows/transformation.py:transformation

"""
from datetime import date
from prefect import flow


@flow
def ingestion(start_date: date):
    print(str(start_date))
