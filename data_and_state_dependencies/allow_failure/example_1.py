from prefect import task, flow, get_run_logger
from prefect.utilities.annotations import allow_failure


@task
def fails():
    raise ValueError("Fail task!")


@task
def bar(y):
    logger = get_run_logger()
    logger.info("Got input: %s", y)
    return y


@task
def clean_up_task():
    logger = get_run_logger()
    logger.info("cleaning up")


@flow
def failure():
    f = fails.submit()
    # `bar` would fail with a `NotReady` state. Now, it will receive an exception
    b = bar.submit(allow_failure(f))
    # assert isinstance(b.result(), ValueError)

    # `bar` would fail with a `NotReady` state. Now, it will run after the upstream completes
    b2 = bar.submit(1, wait_for=[allow_failure(f)])
    print(b2.result())
    # assert b.result() == 1
    clean_up_task.submit(wait_for=[allow_failure(f), allow_failure(b)])


if __name__ == "__main__":
    failure()
