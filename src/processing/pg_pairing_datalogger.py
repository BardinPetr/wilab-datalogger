from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
from typing import List, Callable

from processing.counter import Counter
from processing.datalogger import PhotoGateDatalogger
from processing.interface import InterfaceController


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


class PhotoGatePairingDatalogger(PhotoGateDatalogger):

    def __init__(self, ctrl: InterfaceController):
        super().__init__(ctrl)

        self.tick_history: List[List[TickHistoryItem]] = [[] for _ in range(self.count)]
        self.pair_history: List[PairHistoryItem] = []

        self._pairing_state = PairingState.WAIT_FIRST
        self._pairing_prev_ts = None

    def on_tick(self, uid: int, ts: datetime):
        # print(f"TICK {uid} at {ts.timestamp()}")

        time_ms = self.prepare_time(ts)

        self.tick_history[uid].append(TickHistoryItem(uid, ts, time_ms))
        self._handle_pairing(uid, ts)

        self.fire_update(self.tick_history, self.pair_history)

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
                    self.prepare_time(self._pairing_prev_ts),
                    self.prepare_time(ts)
                ))
