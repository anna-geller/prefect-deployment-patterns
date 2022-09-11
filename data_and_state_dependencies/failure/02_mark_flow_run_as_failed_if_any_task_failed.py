from prefect import flow, task, get_run_logger


@task
def always_fails_task():
    raise ValueError("I fail ❗")


@task
def always_succeeds_task():
    result = "I'm fail safe! ✅ But flow run gets marked as Failed because other task is not as fail-safe"
    logger = get_run_logger()
    logger.info(result)
    return result


@flow
def mark_flow_run_as_failed_if_any_task_failed():
    always_fails_task.submit()
    always_succeeds_task.submit()


if __name__ == "__main__":
    mark_flow_run_as_failed_if_any_task_failed()
