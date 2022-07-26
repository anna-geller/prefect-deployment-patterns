"""
If you provide a string, we will cast it to a Path object for you.
"""
from prefect.deployments import Deployment

Deployment(
    flow="~/flows/healthcheck.py"  # TODO will it find the right flow object though?
)
