import dataclasses
import struct
from enum import IntEnum, Enum
from time import sleep, time
from typing import List, Optional, Iterable

import usb.core

ENDPOINT_READ = 0x81
ENDPOINT_WRITE = 0x1

CMD_REQUEST = 0x09

dev = usb.core.find(idVendor=0x1126, idProduct=0x0004)
dev.reset()

config = dev[0]
# print(config)

interface_id = 0
interface = config.interfaces()[interface_id]
if dev.is_kernel_driver_active(interface_id):
    dev.detach_kernel_driver(interface_id)


def write(data: bytes | List[int]):
    # print(f"WRITE: {bytes(data).hex()}")
    try:
        return dev.write(ENDPOINT_WRITE, data, timeout=100)
    except:
        return False


def read() -> bytes:
    try:
        return bytes(dev.read(ENDPOINT_READ, 64, timeout=1000))
    except:
        return bytes()


def call(cmd: bytes | List[int]) -> bytes:
    write(cmd)
    return read()[:16]


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


def led(r: int, g: int, b: int):
    write([*Commands.LED, 0, r, g, b])


def buzzer(x: bool):
    x = 255 if x else 0
    write([*Commands.BUZZER, x, x])


def voltage_sensor_id(port):
    """
    :param port: number 0-1
    :return: sensor id
    """
    return [0x2, 0x5][port]


# defines which port (0-1) corresponds to which slot
port_map_order: list[Optional[int]] = [None, None]

SLOT_COUNT = 2


def first_empty_slot(default=None):
    slots = sorted({*range(SLOT_COUNT)} - (set(port_map_order) - {None}))
    return slots[0] if len(slots) else default


def map_port(port) -> tuple[int, int]:
    """
    :param port: port number 0-1
    :return: sensor id with mapping order identifier (0x2/0x5 + 0x80) and slot id
    """
    slot = first_empty_slot(default=port_map_order[port])
    port_map_order[port] = slot

    return voltage_sensor_id(port), slot


def unmap_port(port):
    slot = port_map_order[port]
    port_map_order[port] = None
    return slot


def conf(sensor_id: int, slot: int, data: bytes | list[int]):
    if slot == 1:
        sensor_id += 0x80
    write([*Commands.CONF, sensor_id, *data])
    # write([*Commands.CONF_WRITE, *slot.to_bytes(1)])


def config_counter(port: int, threshold: int, mode: int):
    sid, slot = map_port(port)

    threshold = min(5, max(0, threshold))
    threshold = int(threshold / 5 * 0x1000)

    conf(sid, slot, [0x99, 0x09, *mode.to_bytes(1)])
    conf(sid, slot, [*threshold.to_bytes(2, 'little'), *mode.to_bytes(1)])


def unconfig(port: int):
    slot = unmap_port(port)
    conf(0, slot, [0x0] * 8)


def unconfig_all():
    conf(0, 0, [0x0] * 8)
    conf(0, 1, [0x0] * 8)


def get_count(port: int) -> Optional[int]:
    slot = port_map_order[port]
    if slot is None:
        return None

    val = call([ReadPortIdentifiers.READ_COUNT[slot]])
    return val[0]


class CounterType(int, Enum):
    COUNT_FRONT_UP = 0x08
    COUNT_FRONT_UPDOWN = 0x48
    COUNT_FRONT_DOWN = 0x88


class TriggerType(int, Enum):
    TIME_FRONT_UP = 0
    TIME_FRONT_DOWN = 1
    TIME_UP = 2
    TIME_DOWN = 3


def get_interval(port: int, type: int) -> Optional[int]:
    slot = port_map_order[port]
    if slot is None:
        return None

    data = call([*Commands.READ_INTERVAL, ReadPortIdentifiers.READ_INTERVAL[slot] + type])
    data = int.from_bytes(data[:2], 'little')
    data /= 10000
    return data


@dataclasses.dataclass
class Intervals:
    interval_up_front: int
    interval_down_front: int
    time_up: int
    time_down: int

    def __getitem__(self, item: TriggerType):
        return [self.interval_up_front, self.interval_down_front, self.time_up, self.time_down][item]


def get_intervals(port: int) -> Intervals:
    data = [get_interval(port, i) for i in range(4)]
    return Intervals(*data)


def reset_count(port):
    slot = port_map_order[port]
    return write([ReadPortIdentifiers.RESET_COUNT[slot]])


def reset_intervals(port):
    slot = port_map_order[port]
    return write([*Commands.RESET_FREQ, slot])


def get_voltage(i) -> float:
    data = call([*Commands.READ, ReadPortIdentifiers.READ_VOLT[i]])
    data = data[:2]
    v = int.from_bytes(data, 'big')
    return v / (2 ** 14) * 5


config_counter(1, 2, CounterType.COUNT_FRONT_UPDOWN)
config_counter(0, 2, CounterType.COUNT_FRONT_UPDOWN)

i = 0
while True:
    print(get_intervals(0)[TriggerType.TIME_FRONT_UP], get_intervals(1)[TriggerType.TIME_FRONT_UP],
          get_count(0), get_count(1))

    # i += 1
    # if i == 100:
    #     reset_intervals(0)
    #     reset_count(0)
    # if i == 200:
    #     reset_intervals(1)
    #     reset_count(1)
    #
    # if i == 400:
    #     print("U1")
    #     unconfig(1)
    #
    # if i == 500:
    #     print("U0")
    #     unconfig(0)
    #
    # if i == 600:
    #     print("C")
    #
    #     config_counter(0, 2, CounterType.COUNT_FRONT_UPDOWN)
    #     config_counter(1, 2, CounterType.COUNT_FRONT_UPDOWN)
