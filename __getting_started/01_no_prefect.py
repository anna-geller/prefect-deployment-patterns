import logging
import platform
import sys

logging.basicConfig(format="%(asctime)s - [%(levelname)s] - %(message)s", level="INFO")
logger = logging.getLogger(__name__)


def log_platform_info():
    logger.info("Host's network name = %s 📶", platform.node())
    logger.info("Python version = %s 🐍", platform.python_version())
    logger.info("Platform information (instance type) = %s 🚀", platform.platform())
    logger.info("OS/Arch = %s/%s 🤖", sys.platform, platform.machine())


def healthcheck():
    log_platform_info()


if __name__ == "__main__":
    healthcheck()
