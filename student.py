import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    return "".join(random.choices(string.digits, k=8))

@dataclass
class Student:
    name: str
    age: int
    studend_id: str=field(default_factory=generate_id)