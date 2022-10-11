"""
prefect deployment build -n prod -q prod -a flows/transformation.py:transformation
"""
from prefect import flow


@flow
def transformation(dbt_command: str):
    print(dbt_command)
