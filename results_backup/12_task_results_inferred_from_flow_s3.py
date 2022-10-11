from prefect import flow, task


@task
def extract_user() -> str:
    return "Marvin"


@task(retries=2)
def extract_number() -> int:
    return 42


@task(persist_result=False)
def transform(user_name: str, number: int) -> str:
    return f"Welcome, {user_name} to the Club {number}! 👋"


@flow(result_storage="s3/dev")
def my_flow():
    # Both "extract" tasks below have no persistence so this will be inferred from the flow
    user = extract_user()  # ❌ no features requiring persistence, so results won't be persisted
    nr = extract_number()  # ✅ task uses retries, results will be persisted to s3
    final_data = transform(user, nr)  # ❌ persistence manually disabled
    return final_data  # ✅ final flow result will be persisted to S3 using the s3/prod storage block
