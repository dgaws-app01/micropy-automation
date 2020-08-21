import time

class Event:

    def __init__(self, evtName, parentEvt=None, strtNow=True):
        self.evtName = "%s@%d"%(evtName,time.ticks_us())
        if parentEvt:
            self.parentEvt = parentEvt.evtName
        else:
            self.parentEvt = "Main"

        if strtNow:
            self.start()
            self.endTm = None


    def start(self):
        self.strtTm = time.ticks_us()

    def stop(self):
        self.endTm = time.ticks_us()


    def log(self):
        print("%s|S@:%d|E@:%d|D:%d|P:%s"%( self.evtName, self.strtTm, self.endTm, self.endTm - self.strtTm, self.parentEvt))

    def json(self):
        s = """{"Parent":"%s","Name":"%s","Started":"%d","Ended":"%d","Duration":"%d"}"""%(self.parentEvt, self.evtName, self.strtTm, self.endTm, self.endTm - self.strtTm)
        return s

#Examples :
#evt = Event("MachineBootup")
#time.sleep_ms(1900)
#evt2 = Event("WifiScan",evt)
#time.sleep_ms(1400)
#evt2.stop()
#evt.stop()
#evt.log()
#e1Desc = evt.json())
#evt2.log()
#e2Desc = evt2.json())

