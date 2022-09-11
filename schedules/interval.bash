# every 5 min - defined in interval in seconds
prefect deployment build -n prod -q prod -a flows/healthcheck.py:healthcheck --interval 60

# or after the deployment has been created:
prefect deployment set-schedule parametrized/prod --interval 300
