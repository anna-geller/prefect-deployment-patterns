from prefect import flow


@flow(persist_result=True, result_storage="s3/qa")
def flow_persist_result_s3():
    return "Hi from Results and from S3! 🪣"


if __name__ == "__main__":
    flow_persist_result_s3()
