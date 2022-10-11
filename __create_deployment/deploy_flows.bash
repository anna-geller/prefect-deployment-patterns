# DEFAULT STORAGE & INFRASTRUCTURE: locally stored flow code + Local Process; -a stands for --apply; no upload is happening
prefect deployment build -n dev -q dev -a flows/healthcheck.py:healthcheck
prefect deployment build -n dev -q dev -a flows/parametrized.py:parametrized
prefect deployment build -n dev -q dev -a flows/hello.py:hello

# using singleton pattern
prefect agent start -r "dev-.*"
prefect deployment build -n dev -q dev-healthcheck --limit 1 -a flows/healthcheck.py:healthcheck
prefect deployment build -n dev -q dev-parametrized --limit 1 -a flows/parametrized.py:parametrized
prefect deployment build -n dev -q dev-hello --limit 1 -a flows/hello.py:hello
pwq ls --regex "dev.*"


prefect deployment build -n dev -q dev-healthcheck -a flows/healthcheck.py:healthcheck
prefect deployment build -n dev -q dev-parametrized -a flows/parametrized.py:parametrized
prefect deployment build -n dev -q dev-hello -a flows/hello.py:hello
prefect work-queue set-concurrency-limit dev-healthcheck 1
prefect work-queue set-concurrency-limit dev-parametrized 1
prefect work-queue set-concurrency-limit dev-hello 1
prefect agent start -r "dev-.*"


# locally stored flow code + Local Process infra block implicit; no upload is happening
prefect deployment build -n dev -q dev --infra process -a flows/healthcheck.py:healthcheck
prefect deployment build -n dev -q dev --infra process -a flows/parametrized.py:parametrized
prefect deployment build -n dev -q dev --infra process -a flows/hello.py:hello

# locally stored flow code + Local Process infra block explicit; no upload is happening
python blocks/process.py
prefect deployment build -n dev -q dev -ib process/dev -a flows/healthcheck.py:healthcheck
prefect deployment build -n dev -q dev -ib process/dev -a flows/parametrized.py:parametrized
prefect deployment build -n dev -q dev -ib process/dev -a flows/hello.py:hello

# locally stored flow code + Local Process infra block explicit with overrides
prefect deployment build -n dev -q dev -ib process/dev -a flows/healthcheck.py:healthcheck --override env.PREFECT_LOGGING_LEVEL=DEBUG
prefect deployment build -n dev -q dev -ib process/dev -a flows/parametrized.py:parametrized --override env.PREFECT_LOGGING_LEVEL=DEBUG
prefect deployment build -n dev -q dev -ib process/dev -a flows/hello.py:hello --override env.PREFECT_LOGGING_LEVEL=DEBUG

# Using a flow from a nested module ---------------------------------------------------------------
prefect deployment build -n dev -q dev -a flows/some/nested/module.py:import_test

# S3 ---------------------------------------------------------------------------------------------

# upload flow code to S3 storage block + deploy flow as Local Process infra block
python blocks/s3.py
python blocks/process.py
prefect deployment build -n dev -q dev -sb s3/dev -ib process/dev -a flows/healthcheck.py:healthcheck
prefect deployment build -n dev -q dev -sb s3/dev -ib process/dev -a flows/parametrized.py:parametrized --skip-upload
prefect deployment build -n dev -q dev -sb s3/dev -ib process/dev -a flows/hello.py:hello --skip-upload

# upload flow code to S3 storage block + deploy flow as KubernetesJob infra block
python blocks/s3.py
python blocks/k8s.py
prefect deployment build -n dev -q dev -sb s3/dev -ib kubernetes-job/dev -a flows/healthcheck.py:healthcheck
prefect deployment build -n dev -q dev -sb s3/dev -ib kubernetes-job/dev -a flows/parametrized.py:parametrized --skip-upload
prefect deployment build -n dev -q dev -sb s3/dev -ib kubernetes-job/dev -a flows/hello.py:hello --skip-upload

# upload flow code to S3 storage block + deploy flow as DockerContainer infra block
python blocks/s3.py
python blocks/docker.py
prefect deployment build -n dev -q dev -sb s3/dev -ib docker-container/dev -a flows/healthcheck.py:healthcheck
prefect deployment build -n dev -q dev -sb s3/dev -ib docker-container/dev -a flows/parametrized.py:parametrized --skip-upload
prefect deployment build -n dev -q dev -sb s3/dev -ib docker-container/dev -a flows/hello.py:hello --skip-upload

# upload flow code to S3 storage block + deploy flow as ECSTask infra block
python blocks/s3.py
python blocks/docker.py
prefect deployment build -n dev -q dev -sb s3/dev -ib ecs-task/dev -a flows/healthcheck.py:healthcheck
prefect deployment build -n dev -q dev -sb s3/dev -ib ecs-task/dev -a flows/parametrized.py:parametrized --skip-upload
prefect deployment build -n dev -q dev -sb s3/dev -ib ecs-task/dev -a flows/hello.py:hello --skip-upload

# GCS ---------------------------------------------------------------
# upload flow code to GCS storage block + deploy flow as Local Process infra block
python blocks/gcs.py
python blocks/process.py
prefect deployment build -n dev -q dev -sb gcs/dev -ib process/dev -a flows/healthcheck.py:healthcheck
prefect deployment build -n dev -q dev -sb gcs/dev -ib process/dev -a flows/parametrized.py:parametrized --skip-upload
prefect deployment build -n dev -q dev -sb gcs/dev -ib process/dev -a flows/hello.py:hello --skip-upload

# GCS + Docker ---------------------------------------------------------------
# upload flow code to GCS storage block + deploy flow as Local Process infra block
python blocks/gcs.py
python blocks/process.py
prefect deployment build -n dev -q dev -sb gcs/dev -ib docker-container/dev -a flows/healthcheck.py:healthcheck
prefect deployment build -n dev -q dev -sb gcs/dev -ib docker-container/dev -a flows/parametrized.py:parametrized --skip-upload
prefect deployment build -n dev -q dev -sb gcs/dev -ib docker-container/dev -a flows/hello.py:hello --skip-upload

# Azure ---------------------------------------------------------------
# upload flow code to Azure storage block + deploy flow as Local Process infra block
python blocks/azure.py
python blocks/process.py
prefect deployment build -n dev -q dev -sb azure/dev -ib process/dev -a flows/healthcheck.py:healthcheck
prefect deployment build -n dev -q dev -sb azure/dev -ib process/dev -a flows/parametrized.py:parametrized --skip-upload
prefect deployment build -n dev -q dev -sb azure/dev -ib process/dev -a flows/hello.py:hello --skip-upload

# Azure + Docker ---------------------------------------------------------------
# upload flow code to Azure storage block + deploy flow as Local Process infra block
python blocks/azure.py
python blocks/docker_az.py
prefect deployment build -n dev -q dev -sb azure/dev -ib docker-container/az -a flows/healthcheck.py:healthcheck
prefect deployment build -n dev -q dev -sb azure/dev -ib docker-container/az -a flows/parametrized.py:parametrized --skip-upload
prefect deployment build -n dev -q dev -sb azure/dev -ib docker-container/az -a flows/hello.py:hello --skip-upload
# ---------------------------------------------------------------
# run all flows
prefect deployment run healthcheck/dev
prefect deployment run parametrized/dev
prefect deployment run hello/dev

# ---------------------------------------------------------------
# Set schedule directly during build

# run healthcheck flow every minute:
prefect deployment build -n dev -q dev -a flows/healthcheck.py:healthcheck --interval 60

# hourly 9 to 5 during business days (Mon to Fri)
prefect deployment build -n dev -q dev -a flows/parametrized.py:parametrized --cron "0 9-17 * * 1-5"

# daily at 9 AM but only for the next 7 days (e.g. some campaign)
prefect deployment build -n dev -q dev -a flows/hello.py:hello --rrule 'RRULE:FREQ=DAILY;COUNT=7;BYDAY=MO,TU,WE,TH,FR;BYHOUR=9'

# only during business hours
prefect deployment build -n dev -q dev -a flows/hello.py:hello --rrule "FREQ=HOURLY;BYDAY=MO,TU,WE,TH,FR,SA;BYHOUR=9,10,11,12,13,14,15,16,17"

# ---------------------------------------------------------------
# Set schedule in a separate command after build
prefect deployment set-schedule parametrized/dev --interval 300
prefect deployment set-schedule parametrized/dev --cron "*/1 * * * *"  # UTC
prefect deployment set-schedule parametrized/dev --cron '15 20 * * WED' --timezone 'Europe/Berlin'
prefect deployment set-schedule healthcheck/dev --timezone 'Europe/Berlin' --rrule 'RRULE:FREQ=DAILY;COUNT=7;BYDAY=MO,TU,WE,TH,FR;BYHOUR=9'

# ---------------------------------------------------------------
# GitHub storage
prefect deployment build -n dev -q dev -sb github/main -a flows/healthcheck.py:healthcheck
prefect deployment build -n dev -q dev -sb github/main -a flows/parametrized.py:parametrized
prefect deployment build -n dev -q dev -sb github/main -a flows/hello.py:hello

# ---------------------------------------------------------------
# rrule without and with a timezone
prefect deployment build -n dev -q dev -a flows/hello.py:hello --rrule '{"rrule": "DTSTART:20220910T110000\nRRULE:FREQ=HOURLY;BYDAY=MO,TU,WE,TH,FR,SA;BYHOUR=9,10,11,12,13,14,15,16,17"}'
prefect deployment build -n dev -q dev -a flows/hello.py:hello --rrule '{"rrule": "DTSTART:20220910T110000\nRRULE:FREQ=HOURLY;BYDAY=MO,TU,WE,TH,FR,SA;BYHOUR=9,10,11,12,13,14,15,16,17", "timezone": "Europe/Berlin"}'
# ---------------------------------------------------------------
# ECS
prefect deployment build -n dev -q dev -a -ib ecs-task/dev -sb s3/dev flows/healthcheck.py:healthcheck
prefect deployment build -n dev -q dev -a -ib ecs-task/dev -sb s3/dev flows/parametrized.py:parametrized
prefect deployment build -n dev -q dev -a -ib ecs-task/dev -sb s3/dev flows/hello.py:hello

# ---------------------------------------------------------------
# Run parametrized flows from the CLI
prefect deployment build -n dev -q dev -a flows/parametrized.py:parametrized
prefect deployment build -n dev -q dev -a flows/hello.py:hello

prefect deployment run parametrized/dev --param user=Anna --param answer=100
echo '{"user": "World", "answer": 2023}' > params.json
prefect deployment run parametrized/dev --param-file params.json

prefect deployment build -ib cloud-run-job/dev -sb gcs/dev -n dev -q dev -a flows/hello.py:hello