from prefect.blocks.system import JSON

json_block = JSON.load("life-the-universe-everything")
answer = json_block.value["the_answer"]
print(answer)
