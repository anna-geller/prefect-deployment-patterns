import json
from prefect.results import PersistedResultBlob
from prefect.serializers import PickleSerializer, JSONSerializer


def read_result(filename: str, serialier: str = "pickle"):
    path = f"/Users/anna/repos/prefect-deployment-patterns/results/qa/files/{filename}"
    with open(path, "rb") as buffered_reader:
        dict_obj = json.load(buffered_reader)
        blob = PersistedResultBlob.parse_obj(dict_obj)
    if serialier == "json":
        result = JSONSerializer().loads(blob.data)
    else:
        result = PickleSerializer().loads(blob.data)
    return result


if __name__ == "__main__":
    x = "5bb365beb0e2487fbac2c34d378d0882"
    print(read_result(x))
