from prefect.infrastructure import KubernetesJob

k8s_job = KubernetesJob(
    command=["echo", "hello"], labels={"env": "dev", "owner": "anna"}
)
