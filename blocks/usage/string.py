from prefect.blocks.system import String

duck = String.load("duck").value
print(duck)
