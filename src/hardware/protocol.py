from typing import Optional

from hardware.commands import *
from hardware.status import Intervals
from hardware.usb_adapter import USBAdapter
from hardware.slots import SlotManager


class Interface(USBAdapter):

    def __init__(self, on_conn_state):
        super().__init__(on_conn_state)
        self._slot = SlotManager(VOLTAGE_SENSOR_IDS)

    def led(self, r: int, g: int, b: int):
        self.write([*Commands.LED, 0, r, g, b])

    def buzzer(self, x: bool):
        x = 255 if x else 0
        self.write([*Commands.BUZZER, x, x])

    def conf(self, sensor_id: int, slot: int, data: bytes | list[int]):
        if slot == 1:
            sensor_id += 0x80
        self.write([*Commands.CONF, sensor_id, *data])
        # self.write([*Commands.CONF_WRITE, *slot.to_bytes(1)])

    def config_counter(self, port: int, threshold: int, mode: int):
        sid, slot = self._slot.map_port(port)

        threshold = min(5, max(0, threshold))
        threshold = int(threshold / 5 * 0x1000)

        self.conf(sid, slot, [0x99, 0x09, *mode.to_bytes(1)])
        self.conf(sid, slot, [*threshold.to_bytes(2, 'little'), *mode.to_bytes(1)])

    def unconfig(self, port: int):
        slot = self._slot.unmap_port(port)
        self.conf(0, slot, [0x0] * 8)

    def unconfig_all(self):
        self.conf(0, 0, [0x0] * 8)
        self.conf(0, 1, [0x0] * 8)

    def get_count(self, port: int) -> Optional[int]:
        slot = self._slot.slot_by_port(port)
        if slot is None:
            return None

        val = self.call([ReadPortIdentifiers.READ_COUNT[slot]])
        return val[0]

    def get_interval(self, port: int, type: int) -> Optional[int]:
        slot = self._slot.slot_by_port(port)
        if slot is None:
            return None

        data = self.call([*Commands.READ_INTERVAL, ReadPortIdentifiers.READ_INTERVAL[slot] + type])
        data = int.from_bytes(data[:2], 'little')
        data /= 10000
        return data

    def get_all(self, port: int) -> Intervals:
        data = [self.get_interval(port, i) for i in range(4)]
        return Intervals(*data, self.get_count(port))

    def reset_count(self, port):
        slot = self._slot.slot_by_port(port)
        return self.write([ReadPortIdentifiers.RESET_COUNT[slot]])

    def reset_intervals(self, port):
        slot = self._slot.slot_by_port(port)
        return self.write([*Commands.RESET_FREQ, slot])

    def get_voltage(self, i) -> float:
        data = self.call([*Commands.READ, ReadPortIdentifiers.READ_VOLT[i]])
        data = data[:2]
        v = int.from_bytes(data, 'big')
        return v / (2 ** 14) * 5
