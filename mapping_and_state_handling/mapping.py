from prefect import flow, task


@task
def add_one(x: int) -> int:
    return x + 1


@flow
def club_42_plus(x: int = 0) -> int:
    return 42 + x


@flow
def special_flow_for_club_42_members():
    add_one(1)  # returns an int number = 2
    add_one(1, return_state=True)  # returns a Prefect State
    add_one.submit(1)  # returns a Prefect Future, runs through the task runner
    add_one.submit(
        1, return_state=True
    )  # returns a State, runs through the task runner

    # .map() returns a list of Futures, runs through the task runner - futures
    mapped_future = add_one.map(
        [1, 2, 3]
    )
    # # returns State, runs through the task runner
    mapped_future2 = add_one.map(
        mapped_future, return_state=True
    )

    result = club_42_plus()  # returns int = 42
    state = club_42_plus(result, return_state=True)  # Prefect State
    print(state)
    return mapped_future


if __name__ == "__main__":
    x = special_flow_for_club_42_members()
