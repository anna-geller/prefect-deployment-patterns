from prefect.deployments import Deployment
from prefect.orion.schemas.schedules import RRuleSchedule

rrule_string_1 = "DTSTART:20220101T000000\nFREQ=DAILY"
rrule_string_2 = "FREQ=MONTHLY;INTERVAL=1;BYDAY=4SU;COUNT=10"
rrule_string_3 = "FREQ=DAILY;INTERVAL=3;COUNT=10"
rrule_string_4 = """
    DTSTART:20220411T000000
    RRULE:FREQ=WEEKLY;INTERVAL=1;BYDAY=MO,WE,FR;UNTIL=20220630T000000Z
    """

Deployment(
    name="rrule-schedule-deployment",
    flow_location="/path/to/flow.py",
    schedule=RRuleSchedule(rrule="", timezone="America/New_York"),
)
