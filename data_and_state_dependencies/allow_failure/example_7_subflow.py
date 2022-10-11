from prefect import task, flow, get_run_logger, allow_failure


@flow
def fails():
    raise ValueError("Fail task!")


@flow
def clean_up_task():
    logger = get_run_logger()
    logger.info("cleaning up")


@flow
def failure():
    f = fails(return_state=True)
    clean_up_task(allow_failure(f))


failure()
