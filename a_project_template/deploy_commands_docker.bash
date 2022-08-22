cd a_project_template
prefect deployment build flows/healthcheck.py:healthcheck --name docker-simple -q dev -sb s3/dev --infra docker-container -o your.yaml
prefect deployment apply your.yaml
prefect deployment run hello/dev
prefect agent start -q dev
