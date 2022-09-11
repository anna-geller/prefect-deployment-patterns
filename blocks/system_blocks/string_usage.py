from prefect.blocks.system import String

string_block = String.load("duck")
print(string_block.value)
