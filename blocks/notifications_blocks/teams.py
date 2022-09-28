from prefect.blocks.notifications import MicrosoftTeamsWebhook

teams_webhook_block = MicrosoftTeamsWebhook.load("ryan")
teams_webhook_block.notify("Hello from Anna! 👋")
