from prefect import flow, task


@task(retries=2, retry_delay_seconds=2)
def task_infers_to_always_persist_results_from_flow():
    return 42


@flow(persist_result=True)
def flow_with_task_that_infers_results_from_flow():
    task_infers_to_always_persist_results_from_flow()
    return "Hi from Results with task with retries! 👋"


if __name__ == "__main__":
    flow_with_task_that_infers_results_from_flow()
