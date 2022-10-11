from datetime import datetime, timedelta
from prefect.deployments import run_deployment

# trigger a single parametrized run in 5 hours
scheduled_run = run_deployment(
    "scraping/dev",
    scheduled_time=datetime.utcnow() + timedelta(hours=5),
    timeout=0,
    parameters=dict(last_scraped=datetime.utcnow()),
)
