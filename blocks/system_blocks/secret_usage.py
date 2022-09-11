from prefect.blocks.system import Secret

secret_block = Secret.load("prod-rds-mysql-password")

# Access the stored secret
secret_value = secret_block.get()
print(secret_value)
