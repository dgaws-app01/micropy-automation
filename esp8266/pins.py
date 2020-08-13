# Write your code here :-)
import machine
import time

class BoardPinOut:
    def __init__(self, gpio, name, mode, busy = True, aka = ""):
        self.gpio = gpio
        self.name = name
        self.mode = mode
        self.busy = busy
        self.aka = aka
        self.pin = machine.Pin(gpio, mode)
        if busy:
            self.engage()
    
    def engage(self):
        self.busy = True
        
    def release(self):
        self.busy = False
        
    def changeMode(self,mode):
        self.mode = mode
        self.pin = machine.Pin(self.gpio, self.mode)
        
    def on(self):
        if self.mode == machine.Pin.OUT:
            self.pin.on()
    
    def off(self):
        if self.mode == machine.Pin.OUT:
            self.pin.off()
    
    
D0 = BoardPinOut(16, "D0", machine.Pin.OUT, True, "wake,redLED")
D1 = BoardPinOut(5, "D0", machine.Pin.OUT, True, "wake,redLED")

#d0 = {gpio:16, mode:machine.Pin.OUT, busy:True, pin:machine.Pin( gpiopin , machine.Pin.OUT), aka: "wake,redLED"}

D1.on()
time.sleep(1)
D1.off()
time.sleep(1)
D1.on()
time.sleep(1)
D1.off()
