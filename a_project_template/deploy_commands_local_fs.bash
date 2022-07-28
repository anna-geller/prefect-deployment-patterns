cd a_project_template
prefect deployment build flows/hello.py:hello --name local --tag dev
prefect deployment apply deployment.yaml
prefect deployment run hello/local
prefect agent start --tag dev