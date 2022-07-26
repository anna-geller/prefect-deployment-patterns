from prefect import task, flow
from prefect.orion.schemas.states import Completed, Failed


@task
def always_fails_task():
    raise ValueError("I fail successfully")


@task
def always_succeeds_task():
    print("I'm fail safe!")
    return "success"


@flow
def return_state_manually():
    x = always_fails_task.submit().result(raise_on_failure=False)
    y = always_succeeds_task.submit()
    if y.result() == "success":
        return Completed(message="I am happy with this result")
    else:
        return Failed(message="How did this happen!?")


if __name__ == "__main__":
    return_state_manually()
