"""
pip install s3fs
"""
import subprocess
from prefect.filesystems import S3
import shutil
import os
import json
from prefect.results import PersistedResultBlob
from prefect.serializers import PickleSerializer, JSONSerializer

PATH = "/Users/anna/repos/prefect-deployment-patterns/results/qa/files"


def read_result(path: str, serialier: str = "pickle"):
    with open(os.path.join(PATH, path), "rb") as buffered_reader:
        dict_obj = json.load(buffered_reader)
        blob = PersistedResultBlob.parse_obj(dict_obj)
    if serialier == "json":
        result = JSONSerializer().loads(blob.data)
    else:
        result = PickleSerializer().loads(blob.data)
    return result


def set_path():
    subprocess.run(
        f"prefect config set PREFECT_LOCAL_STORAGE_PATH='{PATH}'", shell=True
    )


def clear_result_files():
    shutil.rmtree(PATH)
    os.mkdir(PATH)


def get_result_files():
    out = subprocess.run(f"ls {PATH}", shell=True, capture_output=True)
    files = out.stdout.decode().split("\n")[:-1]
    print(files)
    return files


def get_s3_result_files(bucket_path: str = "s3://prefect-orion/qa/"):
    out = subprocess.run(f"aws s3 ls {bucket_path}", shell=True, capture_output=True)
    files = out.stdout.decode().split("\n")[:-1]
    print(files)
    return files


def clear_s3_result_files(bucket_path: str = "s3://prefect-orion/qa/"):
    subprocess.run(f"aws s3 rm {bucket_path} --recursive", shell=True)


def create_s3_block(name: str = "qa"):
    s3 = S3(bucket_path=f"prefect-orion/{name}")
    uuid = s3.save(name, overwrite=True)
    slug = s3.dict().get("block_type_slug")
    print(f"Created block {slug}/{name} with ID: {uuid}")


def check(check: str, nr_files: int = 0, serializer: str = "pickle"):
    result = get_result_files()
    assert len(result) == nr_files
    print(f"Check {check} passed ✅")
    if result:
        print(f"Result: {read_result(result[0], serializer)}")
        if len(result) == 2:
            print(f"Result: {read_result(result[1], serializer)}")
        clear_result_files()


def check_s3(check: str, nr_files: int = 0):
    assert len(get_s3_result_files()) == nr_files
    print(f"Check {check} passed ✅")
    clear_s3_result_files()


def qa_local_results():
    set_path()
    clear_result_files()

    from flow_dont_persist_result import flow_dont_persist_result
    flow_dont_persist_result()
    check("flow_dont_persist_result", 0)

    from flow_persist_result import flow_persist_result
    flow_persist_result()
    check("flow_persist_result", 1)

    from flow_persist_result_json import flow_persist_result_json
    flow_persist_result_json()
    check("flow_persist_result_json", 1, "json")

    from flow_persist_result_orjson import flow_persist_result_orjson

    flow_persist_result_orjson()
    check("flow_persist_result_orjson", 1, "json")

    from flow_retries_failing_flow import flow_retries_failing_flow

    try:
        flow_retries_failing_flow()
    except:
        pass  # = nothing can get persisted when flow fails
    check("flow_retries_failing_flow", 0)

    from flow_retries_persist_result import flow_retries_persist_result

    flow_retries_persist_result()
    check("flow_retries_persist_result", 1)

    from flow_retries_persist_result_false import flow_retries_persist_result_false

    flow_retries_persist_result_false()
    check("flow_retries_persist_result_false", 0)

    from flow_retries_for_subflow import flow_retries

    flow_retries()
    check("flow_retries_with_subflow", 1)  # result is persisted as it's needed for the subflow

    from flow_persist_result_None import flow_persist_result_None

    flow_persist_result_None()
    check("flow_persist_result_None", 0)

    from task_caching import flow_with_caching_task

    flow_with_caching_task()
    flow_with_caching_task()  # should reuse the result from 1st run
    flow_with_caching_task()  # should reuse the result from 1st run
    check("flow_with_caching_task", 1)

    from task_retries import flow_with_retries_task

    flow_with_retries_task()
    check("flow_with_retries_task", 1)

    from task_persist_result_none import flow_with_task_persist_result_none

    flow_with_task_persist_result_none()
    check("flow_with_task_persist_result_none", 0)

    from task_persist_result_true import flow_with_task_persist_result_true

    flow_with_task_persist_result_true()
    check("flow_with_task_persist_result_true", 1)

    from task_persist_result_false import flow_with_task_persist_result_false

    flow_with_task_persist_result_false()
    check("flow_with_task_persist_result_false", 0)

    from task_persist_result_true_json import flow_with_task_persist_result_true_json
    flow_with_task_persist_result_true_json()
    check("flow_with_task_persist_result_true_json", 1, "json")

    from task_persist_result_true_orjson import flow_with_task_persist_result_true_orjson
    flow_with_task_persist_result_true_orjson()
    check("flow_with_task_persist_result_true_orjson", 1, "json")

    from task_persist_result_true_pickle import flow_with_task_persist_result_true_pickle
    flow_with_task_persist_result_true_pickle()
    check("flow_with_task_persist_result_true_pickle", 1, "pickle")

    from task_and_flow_explicitly_persisting_results import flow_and_task_explicitly_persisting_results
    flow_and_task_explicitly_persisting_results()
    check("flow_explicitly_persisting_results", 2)

    from task_infers_results_from_flow import flow_with_task_that_infers_results_from_flow
    flow_with_task_that_infers_results_from_flow()
    # flow persist results but the task doesn't need persistence because the task run result doesn’t exist until all retries finish
    check("flow_with_task_that_infers_results_from_flow", 1)

    from task_infers_NOT_results_from_flow import flow_with_task_that_does_not_infer_results_from_flow
    flow_with_task_that_does_not_infer_results_from_flow()
    # flow persists, task doesn't persist results
    check("flow_with_task_that_does_not_infer_results_from_flow", 1)

    from task_persist_result_None_flow_False_retries import flow_with_task_with_retries_but_no_results
    flow_with_task_with_retries_but_no_results()
    check("flow_with_task_with_retries_but_no_results", 0)
    print("QA complete!")



def qa_s3_results():
    clear_s3_result_files()
    create_s3_block()

    from flow_dont_persist_result_s3 import flow_dont_persist_result_s3

    flow_dont_persist_result_s3()
    check_s3("flow_dont_persist_result_s3", 0)

    from flow_persist_result_s3 import flow_persist_result_s3

    flow_persist_result_s3()
    check_s3("flow_persist_result_s3", 1)

    from flow_persist_result_s3_json import flow_persist_result_s3_json

    flow_persist_result_s3_json()
    check_s3("flow_persist_result_s3_json", 1)

    from task_persist_result_s3_false import flow_with_task_persist_result_s3_false

    flow_with_task_persist_result_s3_false()
    check_s3("flow_with_task_persist_result_s3_false", 0)

    from task_persist_result_s3_true import flow_with_task_persist_result_s3_true

    flow_with_task_persist_result_s3_true()
    check_s3("task_persist_result_s3_true", 1)


if __name__ == "__main__":
    qa_local_results()
    qa_s3_results()
