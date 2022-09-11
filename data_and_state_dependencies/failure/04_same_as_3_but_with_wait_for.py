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
def one_task_determines_final_state():
    """
    Note that the default ConcurrentTaskRunner will attempt to run both tasks concurrently ❗
    To ensure that unimportant_task always runs before important_task (or the other way around), either:
    1) switch to SequentialTaskRunner: @flow(task_runner=SequentialTaskRunner())
    2) add wait_for attribute to .submit()

    - `result_of_unimportant_task` is an object of type ValueError because with .result() the return value is
    a Python object returned by the task - here: the task returns an exception rather than any data
    - `future_of_important_task` is a PrefectFuture
    """

    result_of_unimportant_task = always_fails_task.submit().result(raise_on_failure=False)  # return value is ValueError exception
    future_of_important_task = always_succeeds_task.submit(wait_for=[result_of_unimportant_task])  # return value is PrefectFuture object
    print(future_of_important_task)
    return future_of_important_task


if __name__ == "__main__":
    one_task_determines_final_state()
