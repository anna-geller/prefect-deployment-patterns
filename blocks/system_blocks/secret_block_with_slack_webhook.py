from prefect import flow, get_run_logger
from prefect.blocks.system import Secret


def add_secret_block():
    secr_block = Secret(value="***")
    secr_block.save(name="SLACK_WEBHOOK_URL")


@flow
def retrieve_secret():
    secret_block = Secret.load("SLACK_WEBHOOK_URL")
    secret_value = secret_block.get()
    masked_secret_value = secret_block.value
    logger = get_run_logger()
    logger.info("Real secret: %s", secret_value)
    logger.info("Masked secret: %s", masked_secret_value)
    # pass downstream
    from prefect_slack import SlackWebhook
    from prefect_slack.messages import send_incoming_webhook_message

    send_incoming_webhook_message(
        slack_webhook=SlackWebhook(secret_value),
        text="Message sent using webhook from a Secret block! :tada:",
    )


if __name__ == "__main__":
    retrieve_secret()
