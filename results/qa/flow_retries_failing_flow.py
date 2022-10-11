from prefect import flow


@flow(retries=3)
def flow_retries_failing_flow():
    raise ValueError("Bad flow")


if __name__ == "__main__":
    flow_retries_failing_flow()
