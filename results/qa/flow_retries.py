from prefect import flow


@flow(retries=3)
def flow_retries():
    return "Hi from Results with retries"


if __name__ == "__main__":
    flow_retries()
