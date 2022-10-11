from prefect import flow, task
from prefect.serializers import JSONSerializer


@task(persist_result=True, result_serializer=JSONSerializer(jsonlib="orjson"))
def task_persist_result_true_orjson():
    return 42


@flow
def flow_with_task_persist_result_true_orjson():
    task_persist_result_true_orjson()
    return "Hi from Results with task with custom JSON serializer! 👋"


if __name__ == "__main__":
    flow_with_task_persist_result_true_orjson()
