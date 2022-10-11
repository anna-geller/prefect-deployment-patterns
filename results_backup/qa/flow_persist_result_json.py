from prefect import flow


@flow(persist_result=True, result_serializer="json")
def flow_persist_result_json():
    return "Hi from Results with JSON serializer! 👋"


if __name__ == "__main__":
    flow_persist_result_json()
