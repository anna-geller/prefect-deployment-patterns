"""
Validating whether s3fs has been installed and with which version
"""
from prefect.infrastructure import KubernetesJob

await KubernetesJob(
    command=["pip", "show", "s3fs"],
    env={"EXTRA_PIP_PACKAGES": "s3fs"},
).run()
