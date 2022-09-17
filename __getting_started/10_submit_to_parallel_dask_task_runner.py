"""
pip install prefect-dask
"""
import time
from random import randint

from prefect import flow, task
from prefect_dask import DaskTaskRunner


@task
def print_number(number):
    time.sleep(randint(0, 3))
    print(number)


@flow(task_runner=DaskTaskRunner())
def crunch_numbers(upper_limit):
    for number in range(upper_limit):
        print_number.submit(number)


if __name__ == "__main__":
    crunch_numbers(7)
