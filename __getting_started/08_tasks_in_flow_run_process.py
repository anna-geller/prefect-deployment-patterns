import time
from random import randint

from prefect import flow, task


@task
def print_number(number):
    time.sleep(randint(0, 3))
    print(number)


@flow
def crunch_numbers(upper_limit):
    for number in range(upper_limit):
        print_number(number)


if __name__ == "__main__":
    crunch_numbers(7)
