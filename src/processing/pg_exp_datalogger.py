from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
from functools import reduce
from itertools import chain
from time import sleep
from typing import List, Callable, Tuple, Optional, Iterable

from hardware.status import Intervals
from processing.counter import Counter
from processing.datalogger import PhotoGateDatalogger
from processing.interface import InterfaceController

ExpSingle = Tuple[int, int]
Experiment = List[List[ExpSingle]]


def flatten(data):
    if isinstance(data, Iterable):
        return reduce(
            lambda acc, i: acc + flatten(i),
            data, []
        )
    return [data]


def exp_as_arr(data):
    for i in range(2):
        data[i] = [*data[i], *([(None, None)] * 2)][:2]
    return flatten(data)


class PhotoGateExpDatalogger(PhotoGateDatalogger):

    def __init__(self, ctrl: InterfaceController):
        super().__init__(ctrl)

        self.history: List[List[int]] = []
        self.current: Optional[Experiment] = None

        self.interface.subscribe_interval_diff(self.on_change)

    def on_tick(self, uid: int, ts: datetime):
        # print("T")
        if self.current is None:
            return

    def on_change(self, uid, is_front, from_opposite, from_same):
        if self.current is None:
            return

        if is_front:
            return

        # print(f"! {uid} at {ts.timestamp()}")
        delta_ms = from_opposite * 1000
        time_ms = self.prepare_time(datetime.now()) - delta_ms
        self.current[uid].append((time_ms, delta_ms))

    def begin(self):
        self.current = [[], []]

    def end(self):
        if self.current is None:
            return

        res = exp_as_arr(self.current)
        print(res)
        self.history.append(res)
        self.fire_update(res)
        self.current = None
