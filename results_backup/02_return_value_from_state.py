from prefect import flow, task


@task
def my_task():
    return 1


@flow
def my_flow():
    state = my_task(return_state=True)
    return state.result() + 1


state = my_flow(return_state=True)
assert state.result() == 2
