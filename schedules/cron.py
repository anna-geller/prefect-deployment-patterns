from prefect.orion.schemas.schedules import CronSchedule

every_2_min = CronSchedule(cron="*/2 * * * *", timezone="US/Eastern")
