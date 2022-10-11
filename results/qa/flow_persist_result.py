from prefect import flow


@flow(persist_result=True)
def flow_persist_result():
    return "Hi from Results! 👋"


if __name__ == "__main__":
    flow_persist_result()
