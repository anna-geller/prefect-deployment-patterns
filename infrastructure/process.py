from prefect.infrastructure import Process
from prefect.deployments import Deployment
from prefect import flow


@flow
def hello_world():
    print("Hello world!")


Deployment(
    name="example",
    flow=hello_world,
    infrastructure=Process(),
)