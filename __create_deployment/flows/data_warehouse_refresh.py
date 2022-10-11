"""
prefect deployment build -n prod -q prod -a flows/ingestion.py:ingestion
prefect deployment build -n prod -q prod -a flows/transformation.py:transformation
prefect deployment build -n prod -q prod -a flows/ml.py:ml
prefect deployment build -n prod -q prod -a flows/data_warehouse_refresh.py:data_warehouse_refresh
"""
from datetime import date, timedelta
from prefect import flow
from prefect.deployments import run_deployment
from prefect.task_runners import SequentialTaskRunner


@flow(task_runner=SequentialTaskRunner())
def data_warehouse_refresh(start_date: date = date.today() - timedelta(days=1)):
    run_deployment(name="ingestion/prod", parameters=dict(start_date=start_date))
    run_deployment(name="transformation/prod", parameters=dict(dbt_command="dbt build"))
    run_deployment(name="ml/prod", timeout=0)  # don't wait for completion


if __name__ == "__main__":
    data_warehouse_refresh()
