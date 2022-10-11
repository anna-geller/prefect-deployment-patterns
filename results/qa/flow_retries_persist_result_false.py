from prefect import flow


@flow(retries=3, persist_result=False)
def flow_retries_persist_result_false():
    return "Hi from Results with retries"


if __name__ == "__main__":
    flow_retries_persist_result_false()
