class Event:

  def __init__(self, evtName, strtNow=True):
    self.evtName = evtName
    if strtNow:
      import time
      self.strtTm = time.ticks_us()
    
  
  def start():
    import time
    self.strtTm = time.ticks_us()
  
  def end():
    pass
  
  def log():
    pass
