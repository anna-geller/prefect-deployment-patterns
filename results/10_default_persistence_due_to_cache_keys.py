from prefect import flow, task
from datetime import timedelta


@task(cache_key_fn=lambda: "always", cache_expiration=timedelta(seconds=20))
def my_task():
    # This task uses caching so its result will be persisted by default
    return "hello world!"


@task
def my_other_task():
    pass


@flow
def my_flow():
    # This task uses a feature that requires result persistence
    my_task()

    # This task does not use a feature that requires result persistence and the
    # flow does not use any features that require task result persistence so its
    # result will not be persisted by default
    my_other_task()
