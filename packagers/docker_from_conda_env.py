# filename: hello_deployment.py
from prefect.deployments import Deployment
from prefect.deployments import FlowScript
from prefect.packaging import DockerPackager
from prefect.software import PythonEnvironment, CondaEnvironment

Deployment(
    flow=FlowScript(path="/path/to/hello_flow.py", name="hello_world"),
    packager=DockerPackager(python_environment=CondaEnvironment.from_environment()),
    name="Hello World",
    tags=["test","docker"],
)
