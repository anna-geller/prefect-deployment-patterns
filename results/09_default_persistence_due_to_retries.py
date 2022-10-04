from prefect import flow, task


@task
def my_task():
    return "hello world!"


@flow(retries=2)
def my_flow():
    # This task does not have persistence toggled off and it is needed for the flow feature,
    # so Prefect will persist its result at runtie
    my_task()
