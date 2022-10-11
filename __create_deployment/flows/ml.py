"""
prefect deployment build -n prod -q prod -a flows/ml.py:ml
"""
from prefect import flow


@flow
def ml():
    print("run ML")
