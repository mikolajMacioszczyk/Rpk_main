from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class RegisterNodeCommand:
    node_id: str = None
    queue_channel: str = None