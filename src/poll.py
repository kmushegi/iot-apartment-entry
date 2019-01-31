import urequests
from time import sleep
from machine import Pin


def start_server():
    API_URL = 'URL TO API ENDPOINT'
    shooter_pin_0 = Pin(12, Pin.OUT)
    shooter_pin_1 = Pin(33, Pin.OUT)
    keep_pressed_seconds = 1.0
    poll_break = 0.5
    press_break = 2.0

    print('Starting DoorUnlock Polling server')

    while(True):
        r = urequests.get(API_URL)
        status = r.json()
        if status.get('unlockStatus', False):
            shooter_pin_0.value(0)
            assert(shooter_pin_0.value() == 0)
            shooter_pin_0.value(1)
            sleep(keep_pressed_seconds)
            shooter_pin_0.value(0)
            assert(shooter_pin_0.value() == 0)
            sleep(press_break)
            shooter_pin_1.value(0)
            assert(shooter_pin_1.value() == 0)
            shooter_pin_1.value(1)
            sleep(keep_pressed_seconds)
            shooter_pin_1.value(0)
            assert(shooter_pin_1.value() == 0)
        sleep(poll_break)
