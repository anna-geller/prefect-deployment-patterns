from prefect import task, flow, get_run_logger, allow_failure


@flow
def fails():
    raise ValueError("Fail task!")


@task
def clean_up_task():
    logger = get_run_logger()
    logger.info("cleaning up")


@flow
def failure():
    f = fails()
    clean_up_task.submit(allow_failure(f))


failure()
