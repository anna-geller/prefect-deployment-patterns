from prefect import flow


@flow(retries=3)
def subflow():
    result = "I'm a subflow 📦"
    print(result)
    return result


@flow(retries=3)
def flow_retries():
    subflow()
    return "Hi from Results with retries and a subflow"


if __name__ == "__main__":
    flow_retries()
