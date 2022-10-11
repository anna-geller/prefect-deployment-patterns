"""
prefect config view --show-defaults
PREFECT_RESULTS_DEFAULT_SERIALIZER='pickle'
PREFECT_LOCAL_STORAGE_PATH='${PREFECT_HOME}/storage'
{
    "serializer": {
        "type": "pickle",
        "picklelib": "cloudpickle",
        "picklelib_version": "2.1.0",
    },
    "data": "gAWVMQAAAAAAAACMLUhpIGZyb20gMTNfYWx3YXlzX3N0b3JlX3Jlc3VsdHNfbG9jYWxseSEg8J+R\ni5Qu\n",
    "prefect_version": "2.4.5+74.gd1f81d15b",
}
"""
from prefect import flow


@flow(persist_result=True)
def always_store_results_locally():
    return "Hi from Results! 👋"


if __name__ == "__main__":
    always_store_results_locally()
