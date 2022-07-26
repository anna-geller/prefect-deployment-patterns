from prefect.filesystems import RemoteFileSystem
from prefect.packaging import FilePackager
from prefect.deployments import Deployment
from flows.healthcheck import run_healthcheck


file_packager = FilePackager(
    filesystem=RemoteFileSystem(
        basepath="gcs://prefect-orion/flows",
    )
)
Deployment(
    flow=run_healthcheck,
    name="gcs",
    packager=file_packager,
)
