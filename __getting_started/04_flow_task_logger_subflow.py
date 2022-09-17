import platform
import sys

from prefect import flow, task, get_run_logger


@task
def log_platform_info():
    logger = get_run_logger()
    logger.info("Host's network name = %s 📶", platform.node())
    logger.info("Python version = %s 🐍", platform.python_version())
    logger.info("Platform information (instance type) = %s 🚀", platform.platform())
    logger.info("OS/Arch = %s/%s 🤖", sys.platform, platform.machine())


@flow
def some_subflow():
    pass


@flow
def healthcheck():
    log_platform_info()
    some_subflow()


if __name__ == "__main__":
    healthcheck()
