from prefect import task, flow, get_run_logger


@task
def get_data_from_source() -> int:
    return 4


@task
def multiply(x: int) -> int:
    return x * 10


@task
def add_two(x: int) -> int:
    return x + 2


@flow
def transform_data(x: int) -> int:
    y = multiply(x)
    z = add_two(y)
    return z


@task
def print_final_output(out: int) -> None:
    logger = get_run_logger()
    logger.info("The final result is %s 🚀", out)


@flow
def process_data():
    raw_data = get_data_from_source()
    final_result = transform_data(raw_data)
    print_final_output(final_result)


if __name__ == "__main__":
    process_data()
