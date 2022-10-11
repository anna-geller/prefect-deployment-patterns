from prefect import flow


@flow(persist_result=False)
def flow_dont_persist_result():
    return "Hi from Results! 👋"


if __name__ == "__main__":
    flow_dont_persist_result()
