from prefect.orion.schemas.schedules import IntervalSchedule
from prefect.deployments import Deployment
from datetime import timedelta
import pendulum
from flows.healthcheck import run_healthcheck

Deployment(
    name="daily-interval-deployment",
    flow=run_healthcheck,
    tags=["interval", "test", "daily"],
    schedule=IntervalSchedule(
        interval=timedelta(days=1),
        anchor_date=pendulum.datetime(2042, 4, 2, 4, 2, 42, tz="America/New_York"),
    ),
)
