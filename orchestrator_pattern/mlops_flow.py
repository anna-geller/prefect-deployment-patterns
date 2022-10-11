"""
prefect deployment build -ib kubernetes-job/gpu -sb s3/dev -n dev -q dev -a flows/ml_training.py:forecast
"""
import pandas as pd
from prefect import flow, task
from prefect.deployments import run_deployment
from prefect.blocks.notifications import SlackWebhook


@task
def extract() -> pd.DataFrame:
    return pd.DataFrame({"user": ["Marvin", "Prefect"], "numbers": ["4", "2"]})


@task
def transform(df) -> pd.DataFrame:
    df["numbers"] = [42, 42]
    return df


@task
def load(df) -> None:
    df.to_parquet("training_data.parquet")


@task
def evaluate_model():
    pass


@task
def load_batch_predictions():
    pass


@task
def generate_final_forecast_report():
    pass


@task
def notify(message: str) -> None:
    webhook = SlackWebhook.load("dev")
    webhook.notify(message)


@flow
def end_to_end_mlops_flow():
    data = extract()
    data = transform(data)
    load(data)
    run_deployment(name="forecast/dev", flow_run_name="ML on K8s with GPU")
    evaluate_model()
    load_batch_predictions()
    generate_final_forecast_report()
    notify("ML pipeline finished! 🚀")


if __name__ == "__main__":
    end_to_end_mlops_flow()
