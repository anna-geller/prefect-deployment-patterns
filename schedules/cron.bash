# hourly from 9 to 5
prefect deployment build -n prod -q prod -a flows/parametrized.py:parametrized --cron "0 9-17 * * 1-5"

# every Wed at 6.30 PM CET - defined after the deployment has been created:
prefect deployment set-schedule parametrized/prod --cron '30 18 * * WED' --timezone 'Europe/Berlin'
