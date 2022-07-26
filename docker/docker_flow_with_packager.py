"""
prefect dev build-image
"""
from prefect import task, flow
from prefect import get_run_logger
from prefect.deployments import Deployment
from prefect.packaging import DockerPackager
from prefect.infrastructure import DockerContainer
from prefect.software import PythonEnvironment


@task
def say_hi(input_: str):
    logger = get_run_logger()
    logger.info("Hello %s!", input_)


@flow
def docker_flow_with_packager(input_: str = "from Docker"):
    say_hi(input_)


Deployment(
    flow=docker_flow_with_packager,
    name="docker_packager",
    packager=DockerPackager(
        base_image="prefecthq/prefect:dev-python3.9",
        python_environment=PythonEnvironment(
            python_version="3.9",
            pip_requirements=["requests"],
        ),
    ),
    infrastructure=DockerContainer(),
)

if __name__ == "__main__":
    docker_flow_with_packager()
