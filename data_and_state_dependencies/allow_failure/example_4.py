from prefect import task, flow, get_run_logger, allow_failure


@task
def upstream(x):
    return x


@task
def downstream(x):
    return x


@flow
def test_flow():
    upstream_state = upstream(1, return_state=True)
    downstream_state = downstream(allow_failure(upstream_state), return_state=True)
    return upstream_state, downstream_state


upstream_state, downstream_state = test_flow()
