from prefect import flow, task


@task
def my_task():
    raise ValueError()


@flow
def my_flow():
    state = my_task(return_state=True)

    if state.is_failed():
        print("Oh no! The task failed. Falling back to '1'.")
        result = 1
    else:
        result = state.result()

    return result + 1


flow_result = my_flow()
assert flow_result == 2
