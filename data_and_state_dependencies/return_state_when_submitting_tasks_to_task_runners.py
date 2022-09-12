from prefect import flow, task, get_run_logger
from prefect.task_runners import ConcurrentTaskRunner


@task
def add_one(x: int) -> int:
    return x + 1


@flow(task_runner=ConcurrentTaskRunner())
def basic_flow_with_task_runner():
    logger = get_run_logger()
    state = add_one.submit(41, return_state=True)  # returns Completed state
    data = state.result()  # gets data from State object: 42
    also_state = add_one.submit(41).wait()  # returns Completed state
    also_data = add_one.submit(41).result()  # returns data: 42
    logger.info("✅ State: %s. Also state: %s", state, also_state)
    logger.info("📊 Data: %s. Also data: %s", data, also_data)


if __name__ == "__main__":
    basic_flow_with_task_runner()
