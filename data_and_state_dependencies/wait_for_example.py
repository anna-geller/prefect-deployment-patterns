from prefect import task, flow


@task
def raw_orders():
    pass


@task
def stg_orders():
    pass


@task
def orders():
    pass


@task
def raw_customers():
    pass


@task
def stg_customers():
    pass


@task
def customers():
    pass


@task
def raw_payments():
    pass


@task
def stg_payments():
    pass


@task
def payments():
    pass


@flow
def dbt():
    orders.submit(wait_for=[stg_orders.submit(wait_for=[raw_orders.submit()])])
    customers.submit(wait_for=[stg_customers.submit(wait_for=[raw_customers.submit()])])
    payments.submit(wait_for=[stg_payments.submit(wait_for=[raw_payments.submit()])])


if __name__ == "__main__":
    dbt()
