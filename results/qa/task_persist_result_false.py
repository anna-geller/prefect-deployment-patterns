from prefect import flow, task


@task(persist_result=False)
def task_persist_result_false():
    return 42


@flow
def flow_with_task_persist_result_false():
    task_persist_result_false()
    return "Hi from Results with task! 👋"


if __name__ == "__main__":
    flow_with_task_persist_result_false()
