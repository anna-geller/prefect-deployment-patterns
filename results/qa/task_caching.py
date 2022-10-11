from datetime import timedelta
from prefect import flow, task
from prefect.tasks import task_input_hash
from typing import Any


@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(seconds=5))
def task_with_short_caching():
    return 42


@flow
def flow_with_caching_task():
    task_with_short_caching()
    return "Hi from Results with task with caching! 👋"


if __name__ == "__main__":
    flow_with_caching_task()
