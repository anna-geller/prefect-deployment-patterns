from prefect.infrastructure import DockerContainer
from prefect.deployments import Deployment
from prefect import flow


@flow
def hello_world():
    print("Hello world!")


Deployment(
    name="example_docker",
    flow=hello_world,
    infrastructure=DockerContainer(),
)