import platform
import sys

from prefect import flow, task, get_run_logger


@task(retries=2, retry_delay_seconds=20)
def log_platform_info():
    logger = get_run_logger()
    logger.info("Host's network name = %s 📶", platform.node())
    logger.info("Python version = %s 🐍", platform.python_version())
    logger.info("Platform information (instance type) = %s 🚀", platform.platform())
    logger.info("OS/Arch = %s/%s 🤖", sys.platform, platform.machine())


@flow(retries=3, retry_delay_seconds=30)
def healthcheck():
    log_platform_info()


if __name__ == "__main__":
    healthcheck()
