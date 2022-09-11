from prefect.blocks.system import JSON

json_block = JSON.load("life-the-universe-everything")
dict_value = json_block.value
print(dict_value)
