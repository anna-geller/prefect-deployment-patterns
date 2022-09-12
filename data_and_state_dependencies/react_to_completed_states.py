from prefect import task, flow
from prefect.blocks.notifications import SlackWebhook


def send_slack_alert(message: str):
    slack_webhook_block = SlackWebhook.load("hq")  # adjust to match your Block name
    slack_webhook_block.notify(message)


@task
def always_succeeds_task():
    return "I'm fail safe! ✅"


@flow
def flow_reacting_to_states():
    state = always_succeeds_task(return_state=True)
    if state.name == "Completed":
        send_slack_alert("Important task completed! 🎉")


if __name__ == "__main__":
    flow_reacting_to_states()
