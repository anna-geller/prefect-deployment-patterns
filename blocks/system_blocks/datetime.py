import pendulum
from prefect.blocks.system import DateTime

block = DateTime(value=pendulum.now(tz="UTC"))
# block = DateTime(value=pendulum.DateTime(2042, 4, 2, 0, 0, 0))
block.save(name="adate", overwrite=True)
