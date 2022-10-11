"""
{
    "serializer": {
        "type": "json",
        "jsonlib": "json",
        "object_encoder": "prefect.serializers.prefect_json_object_encoder",
        "object_decoder": "prefect.serializers.prefect_json_object_decoder",
        "dumps_kwargs": {},
        "loads_kwargs": {},
    },
    "data": '"Hi from Results! \\ud83d\\udc4b"',
    "prefect_version": "2.4.5+74.gd1f81d15b",
}
"""
from prefect import flow


@flow(persist_result=True, result_serializer="json")
def always_store_results_locally():
    return "Hi from Results! 👋"


if __name__ == "__main__":
    always_store_results_locally()
