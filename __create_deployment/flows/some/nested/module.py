from prefect import flow, get_run_logger


@flow
def import_test():
    logger = get_run_logger()
    logger.info("Hi from a nested module")
