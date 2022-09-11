from prefect import task, flow


@task
def always_fails_task():
    raise ValueError("I'm a task that fails successfully")


@task
def always_succeeds_task():
    print("I'm a fail safe task")
    return "foo"


@flow
def always_succeeds_flow():
    print("I'm a fail safe subflow")
    return "bar"


@flow
def subflow_returning_data():
    x = always_fails_task.submit()
    y = always_succeeds_task.submit()
    z = always_succeeds_flow()
    return x, y, z  # Finished in state Completed() - as


if __name__ == "__main__":
    subflow_returning_data()
