from prefect.infrastructure import KubernetesJob

k8s_job = KubernetesJob(
    namespace="prefect",
    customizations=[
        {
            "op": "add",
            "path": "/spec/template/spec/containers/0/resources",
            "value": {"limits": {"memory": "8Gi", "cpu": "4000m"}},
        }
    ],
)
k8s_job.save("prod")
