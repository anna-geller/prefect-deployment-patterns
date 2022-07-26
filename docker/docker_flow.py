"""
prefect dev build-image
"""
from prefect.infrastructure import DockerContainer
from prefect.deployments import Deployment

from flows.healthcheck import run_healthcheck
import subprocess
from pathlib import Path


DEPLOYMENT_NAME = "docker"


Deployment(
    name=DEPLOYMENT_NAME,
    flow=run_healthcheck,
    infrastructure=DockerContainer(
        # image="prefecthq/prefect:dev-python3.10",
        # to use S3 storage block - todo change to your AWS path
        volumes=["/Users/anna/.aws:/root/.aws"],
    ),
)


if __name__ == "__main__":
    subprocess.run(
        f"prefect deployment create {Path(__file__).absolute()}",
        shell=True,
    )
    subprocess.run(
        f"prefect deployment run {run_healthcheck.name}/{DEPLOYMENT_NAME}",
        shell=True,
    )
    subprocess.run(
        "prefect agent start default",
        shell=True,
    )
