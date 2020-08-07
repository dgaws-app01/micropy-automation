import machine
import time
from testimp import p1

o = machine.Pin.OUT
i = machine.Pin.IN

p = machine.Pin(2, o)

print('Imported : %s'%(__name__))

def pn():
    print(__name__)

def start():
    pn()
    p1(p)

if __name__ == "__main__" or __name__ == "main":
    start()
