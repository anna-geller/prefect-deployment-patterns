"""
(dev) ➜  prefect-deployment-patterns git:(main) ✗ aws s3 ls s3://prefect-orion/dev/
(dev) ➜  prefect-deployment-patterns git:(main) ✗ aws s3 ls s3://prefect-orion/dev/
2022-10-07 22:57:56        318 a3fb5486acad4961a90a78fdb61eeae5
"""
from prefect import flow


@flow(persist_result=True, result_serializer="json", result_storage="s3/dev")
def always_store_results_locally():
    return "Hi from Results! 👋"


if __name__ == "__main__":
    always_store_results_locally()
