from prefect import flow
from prefect.serializers import JSONSerializer


@flow(persist_result=True, result_serializer=JSONSerializer(jsonlib="orjson"))
def flow_persist_result_orjson():
    return "Hi from Results with orjson serializer! 👋"


if __name__ == "__main__":
    flow_persist_result_orjson()
