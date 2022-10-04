from prefect import flow, task


@task
def my_task():
    raise ValueError()


@flow
def my_flow():
    try:
        my_task()
    except ValueError:
        print("Oh no! The task failed.")

    return True


my_flow()
