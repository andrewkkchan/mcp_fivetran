from fivetran_connector_sdk import Connector
from fivetran_connector_sdk import Operations as op


def update(configuration: dict, state: dict):
    data = [
        {"id": 1, "name": "John Doe"},
        {"id": 2, "name": "Jane Smith"}
    ]

    for d in data:
        yield op.upsert(table="test_table", data=d)


connector = Connector(update=update)
