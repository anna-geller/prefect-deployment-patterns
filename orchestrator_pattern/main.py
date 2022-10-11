"""
uvicorn main:app --reload
"""
from fastapi import FastAPI
from prefect.deployments import run_deployment

app = FastAPI(title="Sample FastAPI application")


@app.post("/dataflow/")
async def get_data(deployment: str):
    await run_deployment(name=deployment, timeout=0)
    return {"message": f"{deployment} triggered successfully"}
