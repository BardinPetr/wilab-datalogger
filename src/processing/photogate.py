from dataclasses import dataclass
from datetime import datetime
from typing import List

from processing.counter import Counter


@dataclass
class TickHistoryItem:
    uid: int
    ts: datetime


@dataclass
class ChangeHistoryItem(TickHistoryItem):
    value: int


class PhotoGateDatalogger:

    def __init__(self, counters: List[Counter]):
        self._callbacks = []
        self._cnt = len(counters)

        self.tick_history: List[List[TickHistoryItem]] = [[] for _ in range(self._cnt)]

        for counter in counters:
            counter.subscribe(self._on_tick, self._on_update)

    def subscribe(self, on_update):
        self._callbacks.append(on_update)

    def _fire_update(self, *args, **kwargs):
        for i in self._callbacks:
            i(*args, **kwargs)

    def _on_update(self, uid: int, ts: datetime, value: int):
        print(f"UPD  {uid} at {ts.timestamp()} to {value}")

    def _on_tick(self, uid: int, ts: datetime):
        print(f"TICK {uid} at {ts.timestamp()}")
        self.tick_history[uid].append(TickHistoryItem(uid, ts))
        self._fire_update(self.tick_history, [[], []])
