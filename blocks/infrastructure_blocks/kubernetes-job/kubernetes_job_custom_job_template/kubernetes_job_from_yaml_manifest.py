"""
prefect kubernetes manifest flow-run-job >> k8s_flow_run_job_manifest.yaml

Adjust and save it
"""
from prefect.infrastructure import KubernetesJob


k8s_job = KubernetesJob(
    namespace="prefect2",
    image="prefecthq/prefect:2-python3.9",
    env={"EXTRA_PIP_PACKAGES": "s3fs"},
    job=KubernetesJob.job_from_file("k8s_flow_run_job_manifest.yaml"),
)
k8s_job.save("prod", overwrite=True)
