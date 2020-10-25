import uuid


def new_guid() -> str:
    return str(uuid.uuid1())
