from prefect import flow, task


@task(persist_result=True, result_storage="s3/qa")
def task_persist_result_s3_true():
    return 42


@flow
def flow_with_task_persist_result_s3_true():
    task_persist_result_s3_true()
    return "Hi from Results with task! 👋"


if __name__ == "__main__":
    flow_with_task_persist_result_s3_true()
