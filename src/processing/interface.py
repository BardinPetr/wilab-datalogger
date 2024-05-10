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
        self._on_intervals = on_intervals

        self._ctrl = Interface(on_conn_state)

        # self._mp_man = mp.Manager()
        # self._port_status: ListProxy[Intervals] = self._mp_man.list()
        self._port_status: List[Intervals] = []

        for i in range(self.SENSOR_COUNT):
            self._port_status.append(Intervals())

        self.counters = [Counter(i) for i in range(self.SENSOR_COUNT)]

        # self._proc = mp.Process(target=self._run)

    def _init(self):
        self._ctrl.init()
        for i in range(self.SENSOR_COUNT):
            self._ctrl.config_counter(i, self.COUNTER_THRESHOLD, CounterType.COUNT_FRONT_UPDOWN)

    def _run(self):
        self._init()

        while True:
            for i in range(2):
                self._port_status[i] = self._ctrl.get_all(i)
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
