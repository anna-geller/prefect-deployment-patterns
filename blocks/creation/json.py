from prefect.blocks.system import JSON

json_block = JSON(value=dict(the_answer=42))
json_block.save(name="life-the-universe-everything")
