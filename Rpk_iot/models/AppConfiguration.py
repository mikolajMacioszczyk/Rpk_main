from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AppConfiguration:
    node_name: str = None
    queue_host: str = None
    queue_channel: str = None
    server_address: str = None
