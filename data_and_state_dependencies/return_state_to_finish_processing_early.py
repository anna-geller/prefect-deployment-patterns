from prefect import task, flow
from prefect.orion.schemas.states import Completed


@task
def extract_data_from_api():
    return {"result": None}


@task
def process_data(data):
    if isinstance(data["result"], dict):
        pass  # do some processing


@flow
def return_state_manually():
    raw_data = extract_data_from_api()
    if raw_data["result"] is None:
        return Completed(message="No new data available, end the run early")
    else:
        process_data(raw_data)


if __name__ == "__main__":
    return_state_manually()
