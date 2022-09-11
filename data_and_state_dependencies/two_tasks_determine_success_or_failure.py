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
    important_task = always_succeeds_task.submit()
    also_important_task = always_fails_task.submit()
    return important_task, also_important_task


if __name__ == "__main__":
    always_succeeds_flow()
