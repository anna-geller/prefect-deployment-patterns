"""
Starting a MinIO server should output logs including login credentials that can be used as your MINIO_ROOT_USER and MINIO_ROOT_PASSWORD.
"""
from prefect import flow, task
from prefect.deployments import Deployment
from prefect.filesystems import RemoteFileSystem
from prefect.logging import get_run_logger
from prefect.packaging import FilePackager


@task
def greet_world():
    logger = get_run_logger()
    logger.info("Hello world!")


@flow
def give_greeting() -> str:
    greet_world()


minio_packager = FilePackager(
    filesystem=RemoteFileSystem(
        basepath="s3://my-bucket",
        settings={
            "key": "MINIO_ROOT_USER",
            "secret": "MINIO_ROOT_PASSWORD",
            "client_kwargs": {"endpoint_url": "http://localhost:9000"},
        },
    )
)

Deployment(
    flow=give_greeting,
    name="minio_file_package_with_remote_s3fs",
    packager=minio_packager,
)

if __name__ == "__main__":
    give_greeting()
