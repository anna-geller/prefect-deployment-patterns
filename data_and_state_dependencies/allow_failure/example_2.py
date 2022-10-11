from prefect import task, flow, get_run_logger


@task
def fails():
    raise ValueError("Fail task!")


@task
def bar(y):
    return y


@task
def clean_up_task():
    logger = get_run_logger()
    logger.info("cleaning up")


@flow
def test_flow():
    f = fails.submit()
    b = bar.submit(f)
    clean_up_task.submit(wait_for=[b])
    return b


flow_state = test_flow(return_state=True)
task_state = flow_state.result(raise_on_failure=False)
assert task_state.is_pending()
assert task_state.name == "NotReady"
# test_downstream_does_not_run_if_upstream_fails
