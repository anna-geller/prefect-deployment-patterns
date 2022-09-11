from prefect.infrastructure import DockerContainer


docker_block = DockerContainer(
    # for production, it's recommended to pin the image to a specific version e.g. prefecthq/prefect:2.0.5-python3.9
    image="prefecthq/prefect:2-python3.9",  # this will always use the latest Prefect version
    env={"EXTRA_PIP_PACKAGES": "s3fs pandas"},
    image_pull_policy="ALWAYS",  # to always pull latest Prefect 2 image rather than using the one cached locally
    volumes=["/Users/anna/.aws:/root/.aws"],
)
docker_block.save("prod", overwrite=True)
