from prefect import flow, task


@task
def always_fails_task():
    raise ValueError("I fail and immediately end the run 🤒")


@task
def task_that_will_never_run():
    print("Previous blocking task fails so this task will never run")


@flow
def always_failing_flow_with_blocking_task():
    always_fails_task()
    task_that_will_never_run()


if __name__ == "__main__":
    always_failing_flow_with_blocking_task()
