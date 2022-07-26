from prefect.blocks.system import String

block = String(value="Marvin")
block.save(name="duck")
