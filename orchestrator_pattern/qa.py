from datetime import datetime, timedelta
from prefect.coordination_plane import run_deployment, schedule_deployment

run_deployment(
    "parametrized/prod",
    max_polls=0,
    parameters=dict(user="QA Run - not waiting"),
)
run_deployment(
    "parametrized/prod",
    parameters=dict(user="QA Run - waiting"),
)

schedule_deployment(
    "parametrized/prod", schedule_time=datetime.utcnow() + timedelta(minutes=1)
)
schedule_deployment(
    "parametrized/prod",
    schedule_time=datetime.utcnow() + timedelta(minutes=1),
    parameters=dict(user="QA"),
)
