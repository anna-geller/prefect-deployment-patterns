from prefect.blocks.system import Secret

block = Secret(value="SuperStrongPassword42!")
block.save(name="prod-rds-mysql-password")
