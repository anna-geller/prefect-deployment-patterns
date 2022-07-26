from prefect.blocks.system import DateTime
from prefect.blocks.system import EnvironmentVariable

some_date = DateTime.load("adate").value
print(some_date)  # returned as datetime.datetime object
