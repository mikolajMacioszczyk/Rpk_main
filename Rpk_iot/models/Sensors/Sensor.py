from dataclasses import dataclass
from datetime import datetime

from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Sensor:
    sensor_id: str = None
    node_id: str = None
    measurement_time: datetime = None
    sensor_value: float = None
    localization: int = None
    sensor_type: int = None
    sensor_group_guid: str = None
