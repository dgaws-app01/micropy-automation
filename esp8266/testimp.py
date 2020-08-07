import time

print('Imported : %s'%(__name__))

def p1(p):
        print('in p1()')
        while True:
                p.on()
                print('on')
                time.sleep(2)
                p.off()
                print('off')
                time.sleep(1)
