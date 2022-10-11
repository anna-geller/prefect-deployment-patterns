from prefect import flow, task


@task(retries=2)
def task_with_retries():
    return 42


@flow(retries=2)
def flow_with_retries_task():
    task_with_retries()
    return "Hi from Results with task with retries! 👋"


if __name__ == "__main__":
    flow_with_retries_task()
