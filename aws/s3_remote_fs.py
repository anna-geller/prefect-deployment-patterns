from prefect.filesystems import RemoteFileSystem
from prefect.packaging import FilePackager
from prefect.deployments import Deployment
from flows.healthcheck import healthcheck


aws_s3_file_packager = FilePackager(
    filesystem=RemoteFileSystem(
        basepath="s3://my-bucket",
        settings={"key": "AWS_ACCESS_KEY_ID", "secret": "AWS_SECRET_ACCESS_KEY"},
    )
)
Deployment(
    flow=healthcheck,
    name="aws_s3_file_package_with_remote_s3fs",
    packager=aws_s3_file_packager,
)
