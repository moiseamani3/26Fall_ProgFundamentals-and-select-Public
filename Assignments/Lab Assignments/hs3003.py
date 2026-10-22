# hs3003.py - temperature & humidity sensor on the Nano 33 BLE Sense Rev2
# Upload this file to the board, then use it from another script.

import machine
import time

ADDR = 0x44


class HS3003:
    def __init__(self, bus=None):
        if bus is None:
            bus = machine.I2C(1, scl=machine.Pin(15), sda=machine.Pin(14))
        self.bus = bus

    def _read_raw(self):
        self.bus.writeto(ADDR, b'')      # ask the chip for a measurement
        time.sleep_ms(50)                # give it time to finish
        return self.bus.readfrom(ADDR, 4)

    def read(self):
        """Return (temperature_c, humidity_percent)."""
        d = self._read_raw()
        hum = ((d[0] & 0x3F) << 8 | d[1]) * 100 / 16383
        temp = ((d[2] << 8 | d[3]) >> 2) * 165 / 16383 - 40
        return temp, hum

    def temperature(self):
        return self.read()[0]

    def humidity(self):
        return self.read()[1]
