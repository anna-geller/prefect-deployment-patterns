from prefect import flow, task, get_run_logger
from prefect_dbt.cli.commands import trigger_dbt_cli_command
from pathlib import Path


@task
def airbyte_sync_fake():
    logger = get_run_logger()
    logger.info("Running Airbyte sync...")


@flow
def run_dbt():
    airbyte_sync_fake()
    result = trigger_dbt_cli_command(
        "dbt run",
        project_dir=f"{Path(__file__).parent.parent}/dbt_dwh_models",
    )
    return result


if __name__ == "__main__":
    run_dbt()
