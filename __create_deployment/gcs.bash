# upload flow code to GCS storage block + deploy flow as Local Process infra block
python blocks/storage_blocks/gcs.py
python blocks/infrastructure_blocks/process.py
prefect deployment build -n prod -q prod -sb gcs/prod -ib process/prod -a flows/healthcheck.py:healthcheck
prefect deployment build -n prod -q prod -sb gcs/prod -ib process/prod -a flows/parametrized.py:parametrized --skip-upload
prefect deployment build -n prod -q prod -sb gcs/prod -ib process/prod -a flows/hello.py:hello --skip-upload

# Separate projects on GCS with Subpaths ---------------------------------------------------------------
prefect deployment build -n gcs1 -q prod -sb gcs/prod/project1 -ib process/prod -a flows/healthcheck.py:healthcheck -o gcs1.yaml
prefect deployment build -n s31 -q prod -sb s3/prod/project1 -ib process/prod -a flows/healthcheck.py:healthcheck -o s31.yaml

# Separate projects on GCS with Explicit paths ---------------------------------------------------------------
prefect deployment build -n gcs -q prod -sb gcs/prod --path project1 -ib process/prod -a flows/healthcheck.py:healthcheck -o gcs.yaml
prefect deployment build -n s3 -q prod -sb s3/prod --path project1 -ib process/prod -a flows/healthcheck.py:healthcheck -o s3.yaml

prefect deployment run healthcheck/s3
prefect deployment run healthcheck/s31
prefect deployment run healthcheck/gcs
prefect deployment run healthcheck/gcs1


prefect deployment build -n prod -q prod -sb gcs/prod/project2 -ib process/prod -a flows/parametrized.py:parametrized
prefect deployment build -n prod -q prod -sb gcs/prod/project3 -ib process/prod -a flows/hello.py:hello



prefect deployment build -n prod -q prod -sb gcs/prod --path project2 -ib process/prod -a flows/parametrized.py:parametrized
prefect deployment build -n prod -q prod -sb gcs/prod --path project3 -ib process/prod -a flows/hello.py:hello

# Separate projects on S3 ---------------------------------------------------------------
prefect deployment build -n s3 -q prod -sb s3/prod/project1 -ib process/prod -a flows/healthcheck.py:healthcheck
prefect deployment build -n prod -q prod -sb s3/prod/project2 -ib process/prod -a flows/parametrized.py:parametrized
prefect deployment build -n prod -q prod -sb s3/prod/project3 -ib process/prod -a flows/hello.py:hello

# GCS + Docker ---------------------------------------------------------------
# upload flow code to GCS storage block + deploy flow as Local Process infra block
python blocks/gcs.py
python blocks/process.py
prefect deployment build -n prod -q prod -sb gcs/dev -ib docker-container/dev -a flows/healthcheck.py:healthcheck
prefect deployment build -n prod -q prod -sb gcs/dev -ib docker-container/dev -a flows/parametrized.py:parametrized --skip-upload
prefect deployment build -n prod -q prod -sb gcs/dev -ib docker-container/dev -a flows/hello.py:hello --skip-upload

# Azure ---------------------------------------------------------------
# upload flow code to Azure storage block + deploy flow as Local Process infra block
python blocks/azure.py
python blocks/process.py
prefect deployment build -n prod -q prod -sb azure/prod -ib process/prod -a flows/healthcheck.py:healthcheck
prefect deployment build -n prod -q prod -sb azure/prod -ib process/prod -a flows/parametrized.py:parametrized --skip-upload
prefect deployment build -n prod -q prod -sb azure/prod -ib process/prod -a flows/hello.py:hello --skip-upload

# Azure + Docker ---------------------------------------------------------------
# upload flow code to Azure storage block + deploy flow as Local Process infra block
python blocks/azure.py
python blocks/docker_az.py
prefect deployment build -n prod -q prod -sb azure/prod -ib docker-container/az -a flows/healthcheck.py:healthcheck
prefect deployment build -n prod -q prod -sb azure/prod -ib docker-container/az -a flows/parametrized.py:parametrized --skip-upload
prefect deployment build -n prod -q prod -sb azure/prod -ib docker-container/az -a flows/hello.py:hello --skip-upload
# ---------------------------------------------------------------
# run all flows
prefect deployment run healthcheck/prod
prefect deployment run parametrized/prod
prefect deployment run hello/prod

# ---------------------------------------------------------------
# Set schedule directly during build

# run healthcheck flow every minute:
prefect deployment build -n prod -q prod -a flows/healthcheck.py:healthcheck --interval 60

# hourly 9 to 5 during business days (Mon to Fri)
prefect deployment build -n prod -q prod -a flows/parametrized.py:parametrized --cron "0 9-17 * * 1-5"

# daily at 9 AM but only for the next 7 days (e.g. some campaign)
prefect deployment build -n prod -q prod -a flows/hello.py:hello --rrule 'RRULE:FREQ=DAILY;COUNT=7;BYDAY=MO,TU,WE,TH,FR;BYHOUR=9'

# only during business hours
prefect deployment build -n prod -q prod -a flows/hello.py:hello --rrule "FREQ=HOURLY;BYDAY=MO,TU,WE,TH,FR,SA;BYHOUR=9,10,11,12,13,14,15,16,17"

# ---------------------------------------------------------------
# Set schedule in a separate command after build
prefect deployment set-schedule parametrized/prod --interval 300
prefect deployment set-schedule parametrized/prod --cron "*/1 * * * *"  # UTC
prefect deployment set-schedule parametrized/prod --cron '15 20 * * WED' --timezone 'Europe/Berlin'
prefect deployment set-schedule healthcheck/prod --timezone 'Europe/Berlin' --rrule 'RRULE:FREQ=DAILY;COUNT=7;BYDAY=MO,TU,WE,TH,FR;BYHOUR=9'

# ---------------------------------------------------------------
# GitHub storage
prefect deployment build -n prod -q prod -sb github/main -a flows/healthcheck.py:healthcheck
prefect deployment build -n prod -q prod -sb github/main -a flows/parametrized.py:parametrized
prefect deployment build -n prod -q prod -sb github/main -a flows/hello.py:hello

# ---------------------------------------------------------------
# rrule without and with a timezone
prefect deployment build -n prod -q prod -a flows/hello.py:hello --rrule '{"rrule": "DTSTART:20220910T110000\nRRULE:FREQ=HOURLY;BYDAY=MO,TU,WE,TH,FR,SA;BYHOUR=9,10,11,12,13,14,15,16,17"}'
prefect deployment build -n prod -q prod -a flows/hello.py:hello --rrule '{"rrule": "DTSTART:20220910T110000\nRRULE:FREQ=HOURLY;BYDAY=MO,TU,WE,TH,FR,SA;BYHOUR=9,10,11,12,13,14,15,16,17", "timezone": "Europe/Berlin"}'
# ---------------------------------------------------------------
# ECS
prefect deployment build -n prod -q prod -a -ib ecs-task/prod -sb s3/prod flows/healthcheck.py:healthcheck
prefect deployment build -n prod -q prod -a -ib ecs-task/prod -sb s3/prod flows/parametrized.py:parametrized
prefect deployment build -n prod -q prod -a -ib ecs-task/prod -sb s3/prod flows/hello.py:hello

prefect deployment build -n prod -q prod -a flows/healthcheck.py:healthcheck
prefect deployment build -n prod -q prod -a flows/parametrized.py:parametrized
prefect deployment build -n prod -q prod -a flows/hello.py:hello