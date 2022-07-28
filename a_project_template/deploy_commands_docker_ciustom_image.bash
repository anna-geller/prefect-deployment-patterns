cd a_project_template

# Build your image - this can be handled via CI and could be e.g. ECR/ACR registry
docker build -t a_project_template .
docker login -u annaprefect
docker image tag a_project_template:latest annaprefect/a_project_template:latest
docker image push annaprefect/a_project_template:latest

# this creates a block with name "docker-custom-image"
python create_docker_container_block.py

prefect deployment build flows/hello.py:hello --name docker-custom --tag dev -sb s3/dev -ib docker-container/docker-custom-image
prefect deployment apply deployment.yaml
prefect deployment run hello/docker-custom
prefect agent start --tag dev
