import datetime
from dataclasses import dataclass
from functools import cached_property

from helpers import Counter


@dataclass
class Room:
    number: int

@dataclass
class Reservation:
    room: int
    start: datetime.date
    end: datetime.date
    first_name: str
    last_name: str

    @property
    def name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    @cached_property
    def reservation_id(self) -> int:
        return Counter.get_id()
