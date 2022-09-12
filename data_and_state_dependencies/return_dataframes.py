from prefect import flow, task
import pandas as pd


@task
def get_dataframe() -> pd.DataFrame:
    return pd.DataFrame(data={"Users": ["Marvin", "You"]})


@task
def add_points(df: pd.DataFrame) -> pd.DataFrame:
    df["Karma_Points"] = [-42, 100]
    return df


@flow
def process_data() -> pd.DataFrame:
    df = get_dataframe()
    return add_points(df)


if __name__ == "__main__":
    result = process_data()
    print(result)
