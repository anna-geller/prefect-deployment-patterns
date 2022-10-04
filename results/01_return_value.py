from prefect import flow, task


@task
def my_task():
    return 1


@flow
def my_flow():
    task_result = my_task()
    return task_result + 1


result = my_flow()
assert result == 2
