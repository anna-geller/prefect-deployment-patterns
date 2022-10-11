from prefect import flow
from prefect.deployments import run_deployment


@flow
def separate_container_per_run():
    run_deployment(name="my_flow/docker1")
    run_deployment(name="my_flow/docker2")
    run_deployment(name="another_flow/k8s", parameters=dict(gpu=False))
    run_deployment(name="another_flow/k8s_with_gpu", parameters=dict(gpu=True))
