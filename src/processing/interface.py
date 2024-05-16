from time import sleep
from typing import Tuple, List

from hardware.commands import CounterType
from hardware.protocol import Interface
from hardware.status import Intervals
from processing.counter import Counter


class InterfaceController:
    UPDATE_INTERVAL = 0.05  # more than 20Hz is dangerous, as it lowers stability of reads
    COUNTER_THRESHOLD = 2
    SENSOR_COUNT = 2

    def __init__(self, on_conn_state):
        self._running = False
        self._on_conn_state = on_conn_state
        self._on_intervals_differ = None

        self.interface = Interface(self._on_connection_state)

        self._port_status: List[Intervals] = [Intervals() for _ in range(self.SENSOR_COUNT)]
        self.counters = [Counter(i) for i in range(self.SENSOR_COUNT)]

        self._last_intervals: List[Intervals] = None
        self._last_front = [None, None]

    def _on_connection_state(self, is_connected):
        if is_connected:
            self._setup_sensors()
        self._on_conn_state(is_connected)

    def _setup_sensors(self):
        for i in range(self.SENSOR_COUNT):
            self.interface.config_counter(i, self.COUNTER_THRESHOLD, CounterType.COUNT_FRONT_DOWN)

    def subscribe_interval_diff(self, cb):
        self._on_intervals_differ = cb

    def _run(self):
        self.interface.start()

        while self._running:
            for i in range(2):
                data = self.interface.get_all(i)
                if data is None:
                    data = Intervals()

                self._port_status[i] = data
                self.counters[i].external_event(self._port_status[i].counter)

            # self._handle_interval_differ()

            sleep(self.UPDATE_INTERVAL)

    # def _handle_interval_differ(self):
    #     return
    #     if not self._last_intervals:
    #         self._last_intervals = self._port_status[:]
    #         return
    #     if self._last_intervals == self._port_status:
    #         return
    #
    #     uid = 0 if self._last_intervals[0] != self._port_status[0] else 1
    #     last, cur = self._last_intervals[uid], self._port_status[uid]
    #
    #     diffs = [last[i] == cur[i] for i in range(4)]
    #     diff_cnt = sum(diffs)
    #     # print(diff_cnt, *map(int, diffs))
    #
    #     if diff_cnt % 2 != 0:
    #         # print("FC")
    #         return
    #
    #     is_front = last.time_down != cur.time_down
    #
    #     if is_front == self._last_front[uid]:
    #         # print("FF")
    #         return
    #     self._last_front[uid] = is_front
    #
    #     from_opposite = cur.time_down if is_front else cur.time_up
    #     from_same = cur.interval_up_front if is_front else cur.interval_down_front
    #
    #     print(f"{uid=} {is_front=} {from_opposite=} {from_same=}")
    #
    #     self._on_intervals_differ(uid, is_front, from_opposite, from_same)
    #     self._last_intervals = self._port_status[:]

    def get(self) -> Tuple[Intervals, Intervals]:
        return self._port_status[:]

    def reset(self, port: int):
        self.interface.reset_count(port)
        self.interface.reset_intervals(port)
        self.counters[port].reset()

    def reset_freq(self):
        for i in range(self.SENSOR_COUNT):
            self.interface.reset_intervals(i)

    def start(self):
        self._running = True
        self._run()

    def stop(self):
        self._running = False
        self.interface.stop()
