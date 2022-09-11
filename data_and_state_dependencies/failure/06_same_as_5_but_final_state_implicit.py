from prefect import flow, task, get_run_logger


@task
def also_important_task():
    raise ValueError("It's NOT OK if this fails 👎")


@task
def important_task():
    result = "I'm mission critical, but I never fail 🚀"
    logger = get_run_logger()
    logger.info(result)
    return result


@flow
def final_state_determined_implicitly():
    important_task.submit()
    also_important_task.submit()


if __name__ == "__main__":
    final_state_determined_implicitly()
