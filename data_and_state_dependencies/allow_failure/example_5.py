from prefect import task, flow, get_run_logger, allow_failure

# downstream_runs_if_upstream_fails + returns state


@task
def fails():
    raise ValueError("Fail task!")


@task
def bar(y):
    return y


@flow
def test_flow():
    f = fails.submit()
    b = bar(2, wait_for=[allow_failure(f)], return_state=True)
    return b


flow_state = test_flow(return_state=True)
task_state = flow_state.result(raise_on_failure=False)
assert task_state.result() == 2
