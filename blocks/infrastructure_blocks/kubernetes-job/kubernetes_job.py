from prefect.infrastructure import KubernetesJob

k8s = KubernetesJob(
    finished_job_ttl=300,
    image="prefecthq/prefect:2-python3.10",
    namespace="production",
    image_pull_policy="IfNotPresent",
    env={"PREFECT_LOGGING_LEVEL": "INFO"},
)
k8s.save("prod", overwrite=True)
