cd a_project_template
prefect deployment build flows/healthcheck.py:healthcheck --name docker-simple --tag dev -sb s3/dev --infra docker-container
prefect deployment apply deployment.yaml
prefect deployment run hello/dev
prefect agent start --tag dev