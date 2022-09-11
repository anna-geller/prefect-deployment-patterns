from prefect import task, flow


@task
def always_fails_task():
    raise ValueError("I am bad task")


@task
def always_succeeds_task():
    return "foo"


@flow
def always_succeeds_flow():
    return "bar"


@flow
def subflow_returning_state():
    x = always_fails_task.submit()
    y = always_succeeds_task.submit()
    z = always_succeeds_flow(return_state=True)
    return x, y, z  # Finished in state Failed('1/3 states failed.')


if __name__ == "__main__":
    subflow_returning_state()
