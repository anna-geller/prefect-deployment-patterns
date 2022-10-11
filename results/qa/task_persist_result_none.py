from prefect import flow, task


@task
def task_persist_result_none():
    return 42


@flow
def flow_with_task_persist_result_none():
    task_persist_result_none()
    return "Hi from Results with task! 👋"


if __name__ == "__main__":
    flow_with_task_persist_result_none()
