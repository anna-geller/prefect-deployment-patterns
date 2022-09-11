from prefect.orion.schemas.schedules import IntervalSchedule
from prefect.deployments import Deployment
from datetime import timedelta
import pendulum
from flows.your_flow_object import your_flow_object


deployment = Deployment.build_from_flow(
    flow=your_flow_object,
    name="Python Deployment Example",
    schedule=IntervalSchedule(
        interval=timedelta(days=1),
        anchor_date=pendulum.datetime(2042, 4, 2, 4, 2, 42, tz="America/New_York"),
    ),
)

if __name__ == "__main__":
    deployment.apply()
