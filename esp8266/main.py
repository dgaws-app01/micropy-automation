import machine
import time
from testimp import p1

strt_tm = time.ticks_ms()

o = machine.Pin.OUT
i = machine.Pin.IN

p = machine.Pin(2, o)

def pn():
    print(__name__)

def start():
    print('Starting: %s'%(__name__))    
    pn()
    p1(p)

end_tm = time.ticks_ms()
print('%d : Loaded "%s" | MSec Taken : %d '%(strt_tm, __name__, end_tm - strt_tm))

if __name__ == "__main__" or __name__ == "main":
    start()
