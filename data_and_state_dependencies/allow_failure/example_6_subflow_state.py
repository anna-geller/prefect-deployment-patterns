"""
prefect.exceptions.ParameterBindError: Error binding parameters for function 'clean_up_task': too many positional arguments.
Function 'clean_up_task' has signature '' but received args: (<prefect.utilities.annotations.allow_failure object at 0x1439a4b20>,) and kwargs: {}.
"""
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
    f = fails(return_state=True)
    clean_up_task.submit(allow_failure(f))


failure()
