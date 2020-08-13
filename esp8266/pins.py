# Write your code here :-)
import machine
import time

class BoardPinOut:
    def __init__(self, gpio, name, mode, busy = True, aka = "", pinId="L15"):
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
    
    
D0 = BoardPinOut(16, "D0", machine.Pin.OUT, True, "Wake,RedLED", "R15")
D1 = BoardPinOut(5, "D1", machine.Pin.OUT, True, "SCL", "R14")
D2 = BoardPinOut(4, "D2", machine.Pin.OUT, True, "SDA", "R13")
D3 = BoardPinOut(0, "D3", machine.Pin.OUT, True, "FLASH", "R12")
D4 = BoardPinOut(2, "D4", machine.Pin.OUT, True, "TXD1,BlueLED", "R11")

D5 = BoardPinOut(14, "D5", machine.Pin.OUT, True, "SCLK", "R08")
D6 = BoardPinOut(12, "D6", machine.Pin.OUT, True, "MISO", "R07")
D7 = BoardPinOut(13, "D7", machine.Pin.OUT, True, "MOSI", "R06")
D8 = BoardPinOut(15, "D8", machine.Pin.OUT, True, "CS", "R05")

RX = BoardPinOut(3, "RX", machine.Pin.OUT, True, "RXD0", "R04")
TX = BoardPinOut(1, "TX", machine.Pin.OUT, True, "TXD0", "R03")

D = D8
#d0 = {gpio:16, mode:machine.Pin.OUT, busy:True, pin:machine.Pin( gpiopin , machine.Pin.OUT), aka: "wake,redLED"}

i = 0
while i<20:
    D.on()
    time.sleep_ms(50)
    D.off()
    time.sleep_ms(50)
    i = i + 1
