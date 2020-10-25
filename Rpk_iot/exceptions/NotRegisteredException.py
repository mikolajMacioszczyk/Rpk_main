from typing import Any


class NotRegisteredException(Exception):
    def __init__(self, type_name: Any):
        message = f"Instance {type(type_name)} is not registered"
        super().__init__(message)
