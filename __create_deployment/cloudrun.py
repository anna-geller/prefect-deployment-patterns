from prefect_gcp.cloud_run import CloudRunJob


cloud_run_job = CloudRunJob(
    image="us-docker.pkg.dev/cloudrun/container/job:latest",
    credentials=GcpCredentials.load("YOUR_BLOCK_NAME"),
    region="us-central1",
    cpu=256,
    memory=512,
)
cloud_run_job.save("YOUR_BLOCK_NAME")
