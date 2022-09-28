from prefect.blocks.notifications import SlackWebhook

slack_webhook_block = SlackWebhook.load("hq")
slack_webhook_block.notify("Hello from Prefect!")