import time
import network

strt_tm = time.ticks_ms()



end_tm = time.ticks_ms()
print('%d : Loaded "%s" | MSec Taken : %d '%(strt_tm, __name__, end_tm - strt_tm))
