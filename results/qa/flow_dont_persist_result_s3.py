from prefect import flow


@flow(persist_result=False, result_storage="s3/qa")
def flow_dont_persist_result_s3():
    return "Hi from Results! 👋"


if __name__ == "__main__":
    flow_dont_persist_result_s3()
