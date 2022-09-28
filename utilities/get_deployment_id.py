# [Deployment(id=UUID('6a4601dc-f8a4-43ef-8091-f4462a4ad8e2'), name='prod', version='2a2d5609bc55be0840895f50dda05a5b', description=None, flow_id=UUID('ac16a851-a140-47c0-b346-ead3d1366712'), schedule=None, is_schedule_active=True, infra_overrides={}, parameters={}, tags=[], work_queue_name='prod', parameter_openapi_schema={'type': 'object', 'title': 'Parameters', 'properties': {}}, path='/Users/anna/repos/prefect-deployment-patterns/__create_deployment', entrypoint='flows/healthcheck.py:healthcheck', manifest_path=None, storage_document_id=None, infrastructure_document_id=UUID('06cef3c5-0bee-4279-a3a0-2c1d3823014c'))]
import asyncio
from prefect.client import get_client
from prefect.orion.schemas.filters import FlowFilter, DeploymentFilter


async def get_deployment_id(flow_name: str, deployment_name: str = "prod"):
    async with get_client() as client:
        deployments = await client.read_deployments(
            flow_filter=FlowFilter(name={"any_": [flow_name]}),
            deployment_filter=DeploymentFilter(name={"any_": [deployment_name]}),
        )
        id_ = deployments[0].id
        print(id_)
        return id_


if __name__ == "__main__":
    asyncio.run(get_deployment_id("healthcheck"))
