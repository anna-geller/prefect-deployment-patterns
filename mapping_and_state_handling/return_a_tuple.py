from prefect import flow, task


@task
def raise_exception():
    raise ValueError("Hi, I'm an exception!")


@flow
def the_answer():
    return 42


@flow
def main_flow():
    x = raise_exception.submit()
    y = the_answer()
    return x, y


if __name__ == "__main__":
    task1, task2 = main_flow()
