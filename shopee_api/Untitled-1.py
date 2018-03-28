import datetime
import time

ts = time.time()
filename = datetime.datetime.fromtimestamp(ts).strftime('%g%m%d_%H%M%S')
print(filename)
