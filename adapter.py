from time import sleep
from typing import List, Optional

import usb.core


class USBAdapter:
    ENDPOINT_READ = 0x81
    ENDPOINT_WRITE = 0x1

    USB_VID = 0x1126
    USB_PID = 0x0004
    USB_INTERFACE_ID = 0

    def __init__(self):
        self.dev = None
        self._check_connection()

    def connect(self) -> bool:
        print("Connecting")
        try:
            self.dev = usb.core.find(idVendor=self.USB_VID, idProduct=self.USB_PID)
            self.dev.reset()
            if self.dev.is_kernel_driver_active(self.USB_INTERFACE_ID):
                self.dev.detach_kernel_driver(self.USB_INTERFACE_ID)

            print("Connected")
            return True
        except Exception as e:
            print(e)
            print("Connection failed")
            return False

    def _check_connection(self):
        if self.dev:
            return
        if not self.connect():
            sleep(1)
            print("Reconnection...")
            return self._check_connection()

    def write(self, data: bytes | List[int]) -> bool:
        self._check_connection()
        try:
            self.dev.write(self.ENDPOINT_WRITE, data, timeout=100)
            return True
        except:
            self.dev = None
            return False

    def read(self) -> Optional[bytes]:
        self._check_connection()
        try:
            return bytes(self.dev.read(self.ENDPOINT_READ, 64, timeout=1000))
        except:
            self.dev = None
            return None

    def call(self, cmd: bytes | List[int]) -> Optional[bytes]:
        self.write(cmd)
        return self.read()[:16]
