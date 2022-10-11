from prefect import flow, task


@task(persist_result=True)
def task_persisting_results():
    return 42


@flow(persist_result=True)
def flow_and_task_explicitly_persisting_results():
    task_persisting_results()
    return "Hi from Results with task - both persisting results! 👋"


if __name__ == "__main__":
    flow_and_task_explicitly_persisting_results()
