from datetime import datetime, timedelta
from prefect.coordination import run_deployment, schedule_deployment

# run parametrized flow from deployment and wait for its completion before starting the next task
run_deployment(
    "flow_name/deployment_name",
    parameters=dict(user="QA Run - waiting"),
)

# run parametrized flow from deployment and don't wait for completion
run_deployment(
    "flow_name/deployment_name",
    max_polls=0,
    parameters=dict(user="QA Run - not waiting: fire-and-forget"),
)

# schedule deployment run
schedule_deployment(
    "flow_name/deployment_name", schedule_time=datetime.utcnow() + timedelta(minutes=1)
)

# schedule parametrized deployment run
schedule_deployment(
    "flow_name/deployment_name",
    schedule_time=datetime.utcnow() + timedelta(minutes=1),
    parameters=dict(user="QA"),
)
