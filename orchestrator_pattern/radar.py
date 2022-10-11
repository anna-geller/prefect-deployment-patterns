"""
prefect deployment build -n dev -q dev -a flows/parametrized.py:parametrized
"""
from prefect import flow
from prefect.deployments import run_deployment


@flow
def parent_flow_running_deployments():
    run_deployment(name="parametrized/dev")


if __name__ == "__main__":
    parent_flow_running_deployments()
