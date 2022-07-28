cd a_project_template
prefect deployment build flows/hello.py:hello --name dev --tag dev -sb s3/dev
#prefect deployment build flows/hello.py:hello --name hello-dev --tag dev -sb s3/dev --infra docker
prefect deployment apply deployment.yaml
prefect deployment run hello/dev
prefect agent start --tag dev