from prefect.infrastructure import DockerContainer

docker_block = DockerContainer(image="annaprefect/a_project_template:latest")
docker_block.save("docker-custom-image")
