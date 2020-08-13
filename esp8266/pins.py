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

#RX = BoardPinOut(3, "RX", machine.Pin.OUT, True, "RXD0", "R04")
#TX = BoardPinOut(1, "TX", machine.Pin.OUT, True, "TXD0", "R03")

#SD2 = BoardPinOut(9, "SD2", machine.Pin.OUT, True, "SDD2", "L11")
#SD3 = BoardPinOut(10, "SD3", machine.Pin.OUT, True, "SDD3", "L12")

DA = D8
DB = D7

i = 100
while i<20:
    DA.on()
    time.sleep_ms(50)
    DB.on()
    time.sleep_ms(50)
    DA.off()
    time.sleep_ms(50)
    DB.off()
    time.sleep_ms(50)
    i = i + 1
    
D2.on()   
time.sleep(1)
D1.off()
time.sleep(2)
D3.on()
