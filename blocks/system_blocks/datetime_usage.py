from prefect.blocks.system import DateTime

data_time_block = DateTime.load("adate")
print(data_time_block.value)