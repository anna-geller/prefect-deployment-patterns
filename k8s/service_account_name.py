from prefect.infrastructure import KubernetesJob

k8s_job = KubernetesJob(
    namespace="prefect", command=["echo", "hello"], service_account_name="foo"
)
