import multiprocessing as mp
from time import sleep
from typing import Tuple

from commands import CounterType, Intervals
from interface import Interface


class AppController:
    UPDATE_INTERVAL = 0.05
    COUNTER_THRESHOLD = 2
    SENSOR_COUNT = 2

    def __init__(self):
        self._ctrl = Interface()

        self._mp_man = mp.Manager()
        self._port_status = self._mp_man.list()

        for i in range(self.SENSOR_COUNT):
            self._port_status.append(Intervals())

        self._proc = mp.Process(target=self._update)
        self.init()

    def init(self):
        for i in range(self.SENSOR_COUNT):
            self._ctrl.config_counter(i, self.COUNTER_THRESHOLD, CounterType.COUNT_FRONT_UPDOWN)

    def _update(self):
        while True:
            for i in range(2):
                self._port_status[i] = self._ctrl.get_all(i)

            sleep(self.UPDATE_INTERVAL)

    def get(self) -> Tuple[Intervals, Intervals]:
        return self._port_status[:]

    def reset(self, port: int):
        self._ctrl.reset_count(port)
        self._ctrl.reset_intervals(port)

    def start(self):
        self._proc.start()


if __name__ == "__main__":
    i = AppController()
    i.start()


    def q():
        while True:
            sleep(10)
            i.reset(0)


    inp = mp.Process(target=q)
    inp.start()

    while True:
        print(i.get())
        sleep(0.2)
