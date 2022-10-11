from prefect import flow, task

@task
def my_task():
    raise ValueError()

@flow
def my_flow():
    future = my_task.submit()

    try:
        future.result()
    except ValueError:
        print("Ah! Futures will raise the failure as well.")

    # You can ask it not to raise the exception too
    maybe_result = future.result(raise_on_failure=False)
    print(f"Got {type(maybe_result)}")

    return True

my_flow()
from prefect.filesystems import S3