from prefect import flow
from prefect_gcp.cloud_run import CloudRunJob


@flow
def cloud_run_job_flow():
    cloud_run_job = CloudRunJob.load("MY_BLOCK_NAME")
    cloud_run_job.image = "us-docker.pkg.dev/cloudrun/container/custom_image:latest"
    cloud_run_job.command = ["echo", "hello from Prefect!👋"]
    return cloud_run_job.run()
