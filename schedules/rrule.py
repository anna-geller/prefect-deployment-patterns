"""
More examples: https://discourse.prefect.io/tag/rrule
"""
from prefect.deployments import Deployment
from prefect.orion.schemas.schedules import RRuleSchedule
from dateutil.rrule import rrule, DAILY, MO, TU, WE, TH, FR
import pendulum

# start the schedule tomorrow
start_date = pendulum.now().add(days=1)

# daily schedule on weekdays, total of 8 scheduled runs
r_rule = rrule(
    DAILY,
    start_date,
    byweekday=(MO, TU, WE, TH, FR),
    count=8,
)

Deployment(
    name="rrule-schedule-deployment",
    flow_location="/path/to/flow.py",
    schedule=RRuleSchedule.from_rrule(r_rule),
)
