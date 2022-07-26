from prefect import task, flow
from prefect import get_run_logger


@task
def say_hi(user_name: str):
    logger = get_run_logger()
    logger.info("Hello %s!", user_name)


@flow
def hello(user: str = "world"):
    say_hi(user)


if __name__ == "__main__":
    hello(user="Marvin")
