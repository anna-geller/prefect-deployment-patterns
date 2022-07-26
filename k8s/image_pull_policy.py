from prefect.infrastructure import KubernetesJob, KubernetesImagePullPolicy

k8s_job = KubernetesJob(
    namespace="prefect",
    command=["echo", "hello"],
    image_pull_policy=KubernetesImagePullPolicy.IF_NOT_PRESENT,
)
