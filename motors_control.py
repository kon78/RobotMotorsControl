#!/usr/bin/python3
#motors control LM293

from periphery import GPIO
from time import sleep

print ("Motors control script")
print ("Set GPIO line")

#signal
HIGH=1 #TRUE
LOW=0 #FALSE

# Open GPIO /dev/gpiochip1 line 11 direction in/out
#Motor1A --> 11 #GPIO Linux 876
Motor1A = GPIO("/dev/gpiochip1", 11, "out")
#Motor1B --> 13 #924
Motor1B = GPIO("/dev/gpiochip1", 13, "out")
#Motor1E --> 15 #925
Motor1E = GPIO("/dev/gpiochip1", 15, "out")

print ("Going forwards")
Motor1A.write(bool(HIGH))
Motor1B.write(bool(LOW))
Motor1E.write(bool(HIGH))

sleep(2)
print ("Going backwards")
Motor1A.write(bool(LOW))
Motor1B.write(bool(HIGH))
Motor1E.write(bool(HIGH))

sleep(2)
print ("Now stop!")
Motor1E.write(bool(LOW))

Motor1A.close()
Motor1B.close()
Motor1E.close()

#end
