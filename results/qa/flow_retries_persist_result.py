from prefect import flow


@flow(retries=3, persist_result=True)
def flow_retries_persist_result():
    return "Hi from Results with retries"


if __name__ == "__main__":
    flow_retries_persist_result()
