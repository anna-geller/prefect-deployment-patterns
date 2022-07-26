# filename: hello_deployment.py
from prefect.deployments import Deployment
from prefect.deployments import FlowScript
from prefect.packaging import OrionPackager
from prefect.packaging.serializers import PickleSerializer

Deployment(
    flow=FlowScript(path="/path/to/hello_flow.py", name="hello_world"),
    packager=OrionPackager(serializer=PickleSerializer()),
    name="Hello World",
    tags=["test"],
)
