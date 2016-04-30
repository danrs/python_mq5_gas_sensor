# To ust this example, connect your sensor to AIN0.
# If using a grove module and beaglebone grove cape,
# use the J3 grove socket on the cape.

import time
import python_mq5_gas_sensor as mq5

sensor = mq5.mq5() # default pin is AIN0
while True:
    value = sensor.read_raw()
    print "Raw sensor output:",value
    time.sleep(0.2)
