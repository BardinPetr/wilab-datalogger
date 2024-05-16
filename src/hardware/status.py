from dataclasses import dataclass

from hardware.commands import TriggerType


@dataclass
class Intervals:
    interval_up_front: int = 0
    interval_down_front: int = 0
    time_up: int = 0
    time_down: int = 0
    counter: int = 0

    def __getitem__(self, item: TriggerType):
        return [self.interval_up_front, self.interval_down_front, self.time_up, self.time_down, self.counter][item]
