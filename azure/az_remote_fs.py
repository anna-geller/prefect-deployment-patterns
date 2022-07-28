from prefect.filesystems import RemoteFileSystem
from prefect.packaging import FilePackager
from prefect.deployments import Deployment
from flows.healthcheck import healthcheck


file_packager = FilePackager(
    filesystem=RemoteFileSystem(
        basepath="az://prefect",
    )
)
Deployment(
    flow=healthcheck,
    name="az",
    packager=file_packager,
)
