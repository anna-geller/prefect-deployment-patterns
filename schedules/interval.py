from datetime import timedelta
from prefect.orion.schemas.schedules import IntervalSchedule

schedule = IntervalSchedule(interval=timedelta(days=1))
