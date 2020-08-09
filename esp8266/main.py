import machine
import time
from testimp import p1

o = machine.Pin.OUT
i = machine.Pin.IN

p = machine.Pin(2, o)

def pn():
    print(__name__)

def start():
    print('Starting: %s'%(__name__))    
    pn()
    p1(p)

print('Loaded : %s'%(__name__))

if __name__ == "__main__" or __name__ == "main":
    start()
