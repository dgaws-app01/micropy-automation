# Write your code here :-)
import machine
import time

d0 = {gpio:16, mode:machine.Pin.OUT, busy:True, pin:machine.Pin( gpiopin , machine.Pin.OUT), aka: "wake,redLED"}

d0.pin.on()
time.sleep(1)
d0.pin.off()
time.sleep(1)
d0.pin.on()
time.sleep(1)
d0.pin.off()
