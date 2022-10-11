from prefect import flow, task


@task(retries=2, persist_result=False)
def task_infers_results_from_flow():
    return 42


@flow(retries=2, persist_result=True)
def flow_with_task_that_does_not_infer_results_from_flow():
    task_infers_results_from_flow()
    return "Hi from Results with task with retries! 👋"


if __name__ == "__main__":
    flow_with_task_that_does_not_infer_results_from_flow()
