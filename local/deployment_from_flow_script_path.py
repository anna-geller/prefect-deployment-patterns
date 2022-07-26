from prefect.deployments import Deployment
from prefect.deployments import FlowScript
from pathlib import Path

Deployment(
    flow=FlowScript(
        path=Path(__file__).parent / "flows" / "healthcheck.py",
        name="run_healthcheck",  # Optional if the flow can be inferred from the script.
    )
)
