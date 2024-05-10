from time import sleep
from typing import Tuple, List

from hardware.commands import CounterType
from hardware.protocol import Interface
from hardware.status import Intervals
from processing.counter import Counter


class InterfaceController:
    UPDATE_INTERVAL = 0.05
    COUNTER_THRESHOLD = 2
    SENSOR_COUNT = 2

    def __init__(self, on_conn_state, on_intervals):
        self._on_conn_state = on_conn_state
        self._on_intervals = on_intervals

        self._ctrl = Interface(self._on_connection_state)

        self._port_status: List[Intervals] = [Intervals() for _ in range(self.SENSOR_COUNT)]
        self.counters = [Counter(i) for i in range(self.SENSOR_COUNT)]

    def _on_connection_state(self, is_connected):
        if is_connected:
            self._setup_sensors()
        self._on_conn_state(is_connected)

    def _setup_sensors(self):
        for i in range(self.SENSOR_COUNT):
            self._ctrl.config_counter(i, self.COUNTER_THRESHOLD, CounterType.COUNT_FRONT_UPDOWN)

    def _run(self):
        self._ctrl.init()

        while True:
            for i in range(2):
                data = self._ctrl.get_all(i)
                if data is None:
                    data = Intervals()

                self._port_status[i] = data
                self.counters[i].external_event(self._port_status[i].counter)

            self._on_intervals(self._port_status)

            sleep(self.UPDATE_INTERVAL)

    def get(self) -> Tuple[Intervals, Intervals]:
        return self._port_status[:]

    def reset(self, port: int):
        self._ctrl.reset_count(port)
        self._ctrl.reset_intervals(port)
        self.counters[port].reset()

    def start(self):
        # self._proc.start()
        self._run()
