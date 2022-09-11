from machine import Pin
import time
led = Pin(2,Pin.OUT)
led.val(1)
time.sleep(0.5)
led.val(0)
time.sleep(0.5)
