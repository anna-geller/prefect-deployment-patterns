from prefect.deployments import Deployment
from prefect.deployments import FlowScript

Deployment(
    flow=FlowScript(
        path="/Users/anna/repos/prefect-deployment-patterns/flows/healthcheck.py",
        name="run_healthcheck",
    ),
    name="flow_script_dev",
    # tags=["dev"],
)
