"""
https://discourse.prefect.io/t/how-can-i-structure-my-flows-both-in-the-repository-and-the-ui-and-set-project-based-permissions-rbac/706
"""
from prefect import flow, task
from prefect.task_runners import ConcurrentTaskRunner


@task
def crm():
    pass


@task
def erp():
    pass


@task
def google_analytics():
    pass


@task
def shop_system():
    pass


@task
def shipment_api():
    pass


@flow(task_runner=ConcurrentTaskRunner())
def staging_area():
    crm()
    erp()
    google_analytics()
    shop_system()


@flow
def business_vault():
    raise ValueError("Errors in business vault transformations!")


@flow
def data_mart():
    pass


@flow
def data_services():
    pass


@flow(description="Fail immediately if any stage/subflow fails")
def data_warehouse_load():
    staging_area()
    business_vault()
    data_mart()
    data_services()


if __name__ == "__main__":
    data_warehouse_load()
