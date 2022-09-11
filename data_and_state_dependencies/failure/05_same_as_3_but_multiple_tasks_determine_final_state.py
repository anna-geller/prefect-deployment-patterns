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
def two_tasks_determine_final_state():
    future_1 = important_task.submit()
    future_2 = also_important_task.submit()
    return future_1, future_2


if __name__ == "__main__":
    two_tasks_determine_final_state()
