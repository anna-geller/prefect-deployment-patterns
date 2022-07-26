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
    task_im_ok_to_fail = always_fails_task.submit()
    important_task = always_succeeds_task.submit()
    return important_task


if __name__ == "__main__":
    always_succeeds_flow()
