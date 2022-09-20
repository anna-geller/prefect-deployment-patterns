from prefect.infrastructure import KubernetesJob

k8s = KubernetesJob(
    image="prefecthq/prefect:2-python3.10",
    namespace="prod",
    image_pull_policy="IfNotPresent",
    env={"PREFECT_LOGGING_LEVEL": "DEBUG"},
)
k8s.save("prod", overwrite=True)
