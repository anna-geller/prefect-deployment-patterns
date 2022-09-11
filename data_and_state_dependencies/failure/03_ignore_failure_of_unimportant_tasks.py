from prefect import flow, task, get_run_logger


@task
def always_fails_task():
    raise ValueError("It's OK if this fails 👍")


@task
def always_succeeds_task():
    result = "I'm mission critical 🚀"
    logger = get_run_logger()
    logger.info(result)
    return result


@flow
def one_task_determines_success_or_failure():
    """
    Note that the default ConcurrentTaskRunner will attempt to run both tasks concurrently ❗
    To ensure that unimportant_task always runs before important_task, or the other way around,
    either switch to SequentialTaskRunner, or add wait_for attribute
    """
    unimportant_task = always_fails_task.submit()
    important_task = always_succeeds_task.submit()
    return important_task


if __name__ == "__main__":
    one_task_determines_success_or_failure()
