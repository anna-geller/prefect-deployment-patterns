import json
from prefect.results import ResultBlob
from prefect.serializers import PickleSerializer, JSONSerializer


def read_result(filename: str, serialier: str = "pickle"):
    path = f"/Users/anna/repos/prefect-deployment-patterns/results/tmp/{filename}"
    with open(path, "rb") as buffered_reader:
        dict_obj = json.load(buffered_reader)
        blob = ResultBlob.parse_obj(dict_obj)
    if serialier == "json":
        result = JSONSerializer().loads(blob.data)
    else:
        result = PickleSerializer().loads(blob.data)
    return result


if __name__ == "__main__":
    x = "a24a8ba11830422582a157d2e6a17376"
    print(read_result(x))
