"""
More examples: https://discourse.prefect.io/tag/rrule

"DTSTART:20220101T000000\nFREQ=DAILY"
"FREQ=MONTHLY;INTERVAL=1;BYDAY=4SU;COUNT=10"
"FREQ=DAILY;INTERVAL=3;COUNT=10"
"DTSTART:20220411T000000RRULE:FREQ=WEEKLY;INTERVAL=1;BYDAY=MO,WE,FR;UNTIL=20220630T000000Z"

RRuleSchedule(rrule="any_of_above_string_examples", timezone="America/New_York")
"""
from dateutil.rrule import rrule, DAILY, MO, TU, WE, TH, FR
import pendulum
from prefect.deployments import Deployment
from prefect.orion.schemas.schedules import RRuleSchedule
from flows.your_flow_object import your_flow_object

# start the schedule tomorrow
start_date = pendulum.now().add(days=1)

# daily schedule on weekdays, total of 8 scheduled runs
r_rule = rrule(
    DAILY,
    start_date,
    byweekday=(MO, TU, WE, TH, FR),
    count=8,
)
schedule = RRuleSchedule.from_rrule(r_rule)

deployment = Deployment.build_from_flow(
    flow=your_flow_object,
    name="Python Deployment Example",
    schedule=RRuleSchedule.from_rrule(r_rule),
)

if __name__ == "__main__":
    deployment.apply()
