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
    always_succeeds_task.submit(wait_for=[x])
    always_succeeds_flow()


if __name__ == "__main__":
    state = always_fails_flow()
    print(state)
    # (Failed(message='Task run encountered an exception.', type=FAILED, result=ValueError('I fail successfully')),
    # NotReady(message="Upstream task run 'c6fa8d22-8953-4778-8f11-d6e33330dd91' did not reach a 'COMPLETED' state.",
    # type=PENDING, result=None), 42)
