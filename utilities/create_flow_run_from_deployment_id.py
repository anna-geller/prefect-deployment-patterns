import asyncio
from prefect.client import get_client


async def main():
    async with get_client() as client:
        depl_id = "074db2e5-229a-460e-85ad-fca31b379fd2"
        response = await client.create_flow_run_from_deployment(depl_id)
        print(response)


if __name__ == "__main__":
    asyncio.run(main())
