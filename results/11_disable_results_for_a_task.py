import pandas as pd
from prefect import flow, task


@task(persist_result=False)
def my_task() -> pd.DataFrame:
    print("Big dataframe ⛔️ disabling results")


@flow(retries=2)
def my_flow():
    my_task()
