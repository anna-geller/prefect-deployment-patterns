"""
docker run --restart always --name postgres14 --net dev -v postgres_data:/var/lib/postgresql/data -p 5432:5432 -d -e POSTGRES_PASSWORD=postgres postgres:14
"""

from typing import Optional
from prefect.blocks.core import Block
from pydantic import SecretStr


class PostgreSQL(Block):
    _block_type_name = "PostgreSQL Database"
    _logo_url = "https://upload.wikimedia.org/wikipedia/commons/2/2e/Pg_logo.png?h=250"

    user_name: SecretStr
    password: SecretStr
    db_name: Optional[str] = "postgres"
    db_hostname: Optional[str] = "localhost"
    db_port: Optional[int] = 5432

    def get_connection_string(self):
        usr = self.user_name.get_secret_value()
        pwd = self.password.get_secret_value()
        return (
            f"postgresql://{usr}:{pwd}@{self.db_hostname}:{self.db_port}/{self.db_name}"
        )


def create_postgres_block():
    postgres_block = PostgreSQL(user_name="postgres", password="postgres")
    postgres_block.save("dev")


def read_postgres_block():
    postgres_block = PostgreSQL.load("dev")
    return postgres_block.get_connection_string()


if __name__ == "__main__":
    create_postgres_block()
