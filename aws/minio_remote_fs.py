from prefect.filesystems import RemoteFileSystem
from prefect.packaging import FilePackager
from prefect.deployments import Deployment
from flows.healthcheck import run_healthcheck


minio_file_packager = FilePackager(
    filesystem=RemoteFileSystem(
        basepath="s3://my-bucket",
        settings={
            "key": "MINIO_ROOT_USER",
            "secret": "MINIO_ROOT_PASSWORD",
            "client_kwargs": {"endpoint_url": "http://localhost:9000"}
        }
    )
)
Deployment(
    flow=run_healthcheck,
    name="minio_file_package_with_remote_s3fs",
    packager=minio_file_packager
)
