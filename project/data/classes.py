from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class MyInput:
    num_intervals: int
    interval_start: int
    interval_end: int
    percision: int

@dataclass_json
@dataclass
class MyOutput:
    result: str
    compute_time: str
    percision: str