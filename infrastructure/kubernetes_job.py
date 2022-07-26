from prefect.infrastructure import KubernetesJob
from prefect.deployments import Deployment
from prefect import flow


@flow
def hello_world():
    print("Hello world!")


Deployment(
    name="example_kubernetes",
    flow=hello_world,
    infrastructure=KubernetesJob(),
)