"""
No results get stored here
"""
from prefect import flow, task


@task(persist_result=False)
def my_task():
    print("Big dataframe ⛔️ disabling results")


@flow(retries=2)
def my_flow():
    my_task()


if __name__ == "__main__":
    my_flow()
