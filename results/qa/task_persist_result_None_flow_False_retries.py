from prefect import flow, task


@task(retries=2)
def task_persist_result_none_but_needs_results_for_retries():
    return 42


@flow(persist_result=False)
def flow_with_task_with_retries_but_no_results():
    task_persist_result_none_but_needs_results_for_retries()
    return "Hi from Results with task! 👋"


if __name__ == "__main__":
    flow_with_task_with_retries_but_no_results()
