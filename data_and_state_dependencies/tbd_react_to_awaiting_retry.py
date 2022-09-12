from prefect import task, flow
from prefect.blocks.notifications import SlackWebhook


def send_slack_alert(message: str):
    slack_webhook_block = SlackWebhook.load("hq")
    slack_webhook_block.notify(message)


@task(retries=2, retry_delay_seconds=1)
def always_failing_task():
    return 1 / 0


@flow
def flow_reacting_to_retries():
    future = always_failing_task.submit()
    state = future.wait()
    if state.name == "AwaitingRetry":
        send_slack_alert(f"Task X will be retried 🔄")  # doesn't work
    if state.name == "Retrying":
        send_slack_alert(f"Task X is getting retried 🔄")  # doesn't work
    if state.name == "Failed":
        send_slack_alert(f"Task X failed ❗")  # works
    if state.is_failed():
        send_slack_alert(f"Task X failed ❗")  # works too


if __name__ == "__main__":
    flow_reacting_to_retries()
