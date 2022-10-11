from prefect import flow, task


@task
def my_task():
    return "Hello"


@flow(persist_result=True, result_serializer="json")
def infer_whether_to_store_results():
    my_task()  # This task will use the flow's result storage


if __name__ == "__main__":
    infer_whether_to_store_results()
