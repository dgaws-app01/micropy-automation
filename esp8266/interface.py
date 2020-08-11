import time
import network
#import config file

strt_tm = time.ticks_ms()

# if config.type = "ROOT"
  # connect to WIFI , SSID = config.parentname
# if config.type = "BRANCH"
  # connect to WIFI, SSID = config.parentname + config.parentIndex
  # also setup as AP, AP-SSID = config.name + config.index
# if config.type = "LEAF"
  # connect to WIFI, SSID = config.parentname + config.parentIndex
  
#print all details related to network - interface Status, Connectivity Stat , IP, MAC, Signal

end_tm = time.ticks_ms()
print('%d : Loaded "%s" | MSec Taken : %d '%(strt_tm, __name__, end_tm - strt_tm))
