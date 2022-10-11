from prefect import flow


@flow(persist_result=True, result_storage="s3/dev", result_serializer="json")
def flow_persist_result_s3_json():
    return "Hi from Results and from S3 🪣 and JSON 🚀"


if __name__ == "__main__":
    flow_persist_result_s3_json()
