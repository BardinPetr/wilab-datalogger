from typing import Optional, List


class SlotManager:

    def __init__(self, sensor_ids: List[int]):
        self.count = len(sensor_ids)
        self.sensor_ids = sensor_ids
        self._port_map_order: list[Optional[int]] = [None for _ in range(self.count)]

    def first_empty_slot(self, default=None):
        slots = sorted({*range(self.count)} - (set(self._port_map_order) - {None}))
        return slots[0] if len(slots) else default

    def map_port(self, port: int) -> tuple[int, int]:
        """
        :param port: port number 0-1
        :return: sensor id with mapping order identifier (0x2/0x5 + 0x80) and slot id
        """
        slot = self.first_empty_slot(default=self._port_map_order[port])
        self._port_map_order[port] = slot
        return self.sensor_ids[port], slot

    def unmap_port(self, port: int):
        slot = self._port_map_order[port]
        self._port_map_order[port] = None
        return slot

    def slot_by_port(self, port) -> int:
        return self._port_map_order[port]
