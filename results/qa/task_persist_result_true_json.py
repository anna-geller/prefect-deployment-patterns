from prefect import flow, task


@task(persist_result=True, result_serializer="json")
def task_persist_result_true_json():
    return 42


@flow
def flow_with_task_persist_result_true_json():
    task_persist_result_true_json()
    return "Hi from Results with task with JSON serializer! 👋"


if __name__ == "__main__":
    flow_with_task_persist_result_true_json()
