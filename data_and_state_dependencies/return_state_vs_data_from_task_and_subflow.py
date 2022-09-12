from prefect import flow, task, get_run_logger


@task
def add_one(x: int) -> int:
    return x + 1


@flow
def subflow_returning_data(emoji: str = "🚀") -> str:
    return f"Subflows are {emoji}!"


@flow
def basic_flow():
    logger = get_run_logger()
    state = add_one(41, return_state=True)  # returns Completed state
    data = state.result()  # get data from State object: 42
    also_data = add_one(41)  # returns data directly: 42
    logger.info("✅ State: %s.", state)
    logger.info("📊 Data: %s. Also data: %s", data, also_data)
    # the same works exactly the same way with subflows:
    state_of_a_subflow = subflow_returning_data("😎", return_state=True)
    subflow_data = state_of_a_subflow.result()
    also_subflow_data = subflow_returning_data("💙️")
    logger.info("✅️ Subflow state: %s.", state_of_a_subflow)
    logger.info(
        "📊 Subflow data: : %s. Also subflow data: %s",
        subflow_data,
        also_subflow_data,
    )


if __name__ == "__main__":
    basic_flow()
