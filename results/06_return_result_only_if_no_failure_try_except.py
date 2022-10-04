from prefect import flow, task


@task
def my_task():
    raise ValueError()


@flow
def my_flow():
    state = my_task(return_state=True)

    try:
        result = state.result()
    except ValueError:
        print("Oh no! The state raised the error!")

    return True


final_result = my_flow()
print(final_result)
