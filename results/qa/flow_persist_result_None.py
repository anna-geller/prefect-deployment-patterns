from prefect import flow


@flow
def flow_persist_result_None():
    return "Hi from Results! 👋"


if __name__ == "__main__":
    flow_persist_result_None()
