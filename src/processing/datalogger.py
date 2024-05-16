from datetime import datetime

from processing.interface import InterfaceController


class PhotoGateDatalogger:

    def __init__(self, ctrl: InterfaceController):
        self.__callbacks = []
        self.__enable = False
        self.interface = ctrl
        self.count = len(self.interface.counters)

        for counter in self.interface.counters:
            counter.subscribe(self._on_event)

        self._time_base = None
        self.zero_time()

    def zero_time(self):
        self._time_base = datetime.now()

    def prepare_time(self, ts: datetime):
        return round((ts - self._time_base).total_seconds() * 1000)

    def _on_event(self, *args):
        if self.__enable:
            self.on_tick(*args)

    def enable(self, enable):
        self.__enable = enable

    def subscribe(self, on_update):
        self.__callbacks.append(on_update)

    def fire_update(self, *args, **kwargs):
        for i in self.__callbacks:
            i(*args, **kwargs)

    def on_tick(self, uid: int, ts: datetime):
        print(f"TICK {uid} at {ts.timestamp()}")
