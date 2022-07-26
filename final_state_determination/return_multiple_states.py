from prefect import flow, task


@task
def always_fails_task():
    raise ValueError("I fail successfully")


@task
def always_succeeds_task():
    print("I'm fail safe!")
    return "success"


@flow
def always_succeeds_flow():
    return 42


@flow
def always_fails_flow():
    x = always_fails_task.submit()  # .result(raise_on_failure=False)
    y = always_succeeds_task.submit()  # wait_for=[x])
    z = always_succeeds_flow()
    return x, y, z


if __name__ == "__main__":
    state = always_fails_flow()
    print(state)
