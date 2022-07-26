from prefect import flow, task


@task
def always_fails_task():
    raise ValueError("I fail successfully")


@task
def always_succeeds_task():
    print("I'm fail safe!")
    return "success"


@flow
def always_fails_flow():
    always_fails_task.submit().result(raise_on_failure=False)
    always_succeeds_task()


if __name__ == "__main__":
    always_fails_flow()
