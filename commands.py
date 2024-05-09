from dataclasses import dataclass
from enum import Enum


class Commands(list, Enum):
    HW_VERSION = [0x17]
    SW_VERSION = [0x04]
    LED = [0x26, 0x02]
    BUZZER = [0x28]
    CONF = [0x0a]
    CONF_WRITE = [0x2a]
    READ = [0x03]
    READ_INTERVAL = [0x1c]
    RESET_FREQ = [0x22]


class ReadPortIdentifiers(list, Enum):
    READ_COUNT = [0x09, 0x1e]
    READ_INTERVAL = [0x01, 0x05]
    READ_VOLT = [0x02, 0x05]
    RESET_COUNT = [0x07, 0x1f]


class CounterType(int, Enum):
    COUNT_FRONT_UP = 0x08
    COUNT_FRONT_UPDOWN = 0x48
    COUNT_FRONT_DOWN = 0x88


class TriggerType(int, Enum):
    TIME_FRONT_UP = 0
    TIME_FRONT_DOWN = 1
    TIME_UP = 2
    TIME_DOWN = 3


@dataclass
class Intervals:
    interval_up_front: int = 0
    interval_down_front: int = 0
    time_up: int = 0
    time_down: int = 0
    counter: int = 0

    def __getitem__(self, item: TriggerType):
        return [self.interval_up_front, self.interval_down_front, self.time_up, self.time_down][item]


# @dataclass
# class SensorStatus:

VOLTAGE_SENSOR_IDS = [0x2, 0x5]
