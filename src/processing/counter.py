from datetime import datetime
from typing import Dict, Callable, List


class Counter:

    def __init__(self, uid: int):
        self.uid = uid
        self._current: int = 0
        self._handlers: Dict[str, List[Callable]] = {
            'tick':   [],
            'update': []
        }

    def subscribe(self, on_tick, on_update):
        self._handlers['tick'].append(on_tick)
        self._handlers['update'].append(on_update)

    def _fire(self, evt: str, ts: datetime, *args, **kwargs):
        for cb in self._handlers[evt]:
            cb(self.uid, ts, *args, **kwargs)

    def external_event(self, new_val: int):
        ts = datetime.now()

        diff = new_val - self._current
        if diff == 0:
            return

        if diff > 0:
            for _ in range(diff):
                self._fire('tick', ts)

        self._fire('update', ts, new_val)
        self._current = new_val

    def reset(self):
        self._fire('update', datetime.now(), 0)
        self._current = 0
