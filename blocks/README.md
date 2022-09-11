Many `DockerContainer` and `KubernetesJob` blocks examples shown in this directory leverage the Prefect image `prefecthq/prefect:2-python3.9`

For production use cases, we recommend picking specific tags related to a concrete Prefect version e.g.: `prefecthq/prefect:2.4.0-python3.9`


For a recipe storing flow code in a Docker image (rather than using a remote storage block), check:
- [the release blog post](https://medium.com/the-prefect-blog/prefect-2-3-0-adds-support-for-flows-defined-in-docker-images-and-github-repositories-79a8797a7371)
- [the template repository](https://github.com/anna-geller/prefect-docker-deployment)

