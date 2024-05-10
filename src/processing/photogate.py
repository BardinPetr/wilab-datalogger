from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
from typing import List

from processing.counter import Counter


@dataclass
class TickHistoryItem:
    uid: int
    ts: datetime
    relative_ms: int


@dataclass
class PairHistoryItem:
    start_ts: datetime
    end_ts: datetime
    start_relative: int
    end_relative: int

    def __post_init__(self):
        self.duration = self.end_relative - self.start_relative


class PairingState(IntEnum):
    WAIT_FIRST = 0
    WAIT_SECOND = 1


class PhotoGateDatalogger:

    def __init__(self, counters: List[Counter]):
        self._callbacks = []
        self._cnt = len(counters)
        self._time_base = 0

        self.tick_history: List[List[TickHistoryItem]] = [[] for _ in range(self._cnt)]
        self.pair_history: List[PairHistoryItem] = []

        self._pairing_state = PairingState.WAIT_FIRST
        self._pairing_prev_ts = None

        for counter in counters:
            counter.subscribe(self._on_tick, self._on_update)

        self.zero_time()

    def zero_time(self):
        self._time_base = datetime.now()

    def _prepare_time(self, ts: datetime):
        return round((ts - self._time_base).total_seconds() * 1000)

    def subscribe(self, on_update):
        self._callbacks.append(on_update)

    def _fire_update(self, *args, **kwargs):
        for i in self._callbacks:
            i(*args, **kwargs)

    def _on_update(self, uid: int, ts: datetime, value: int):
        print(f"UPD  {uid} at {ts.timestamp()} to {value}")

    def _on_tick(self, uid: int, ts: datetime):
        print(f"TICK {uid} at {ts.timestamp()}")

        time_ms = self._prepare_time(ts)

        self.tick_history[uid].append(TickHistoryItem(uid, ts, time_ms))
        self._handle_pairing(uid, ts)

        self._fire_update(self.tick_history, self.pair_history)

    def _handle_pairing(self, uid: int, ts: datetime):
        if uid == 0:
            self._pairing_prev_ts = ts
            self._pairing_state = PairingState.WAIT_SECOND
        else:
            if self._pairing_state == PairingState.WAIT_SECOND:
                self._pairing_state = PairingState.WAIT_FIRST
                self.pair_history.append(PairHistoryItem(
                    self._pairing_prev_ts,
                    ts,
                    self._prepare_time(self._pairing_prev_ts),
                    self._prepare_time(ts)
                ))
