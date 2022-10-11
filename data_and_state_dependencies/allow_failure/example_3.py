from prefect import task, flow, get_run_logger, allow_failure
# from prefect.utilities.annotations import allow_failure


@task
def fails():
    raise ValueError("Fail task!")


@task
def bar(y):
    return y


@task
def clean_up_task():
    logger = get_run_logger()
    logger.info("cleaning up")


@flow
def failure():
    f = fails.submit()
    b = bar.submit(allow_failure(f))
    clean_up_task.submit(wait_for=[allow_failure(f), allow_failure(b)])
    return b.result()


result = failure()  # ValueError('Fail task!')
assert isinstance(result, ValueError)
assert "Fail task!" in str(result)
# test_downstream_receives_exception_if_upstream_fails_and_allow_failure
