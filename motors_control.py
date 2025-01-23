#!/usr/bin/python3
#motors control LM293

from periphery import GPIO
from time import sleep

print ("Motors control script")
print ("Set GPIO line")

#signal
HIGH=1 #TRUE
LOW=0 #FALSE

#left motor
# Open GPIO /dev/gpiochip1 line 11 direction in/out
#Motor1A --> 11 #GPIO Linux 876
Motor1A = GPIO("/dev/gpiochip1", 11, "out")
#Motor1B --> 13 #924
Motor1B = GPIO("/dev/gpiochip1", 13, "out")
#Motor1E --> 15 #925
Motor1E = GPIO("/dev/gpiochip1", 15, "out")

#right motor
#Motors2A --> 19 #GPIO Linux 871
Motor2A = GPIO("/dev/gpiochip1", 19, "out")
#Motors2B --> 21 #GPIO Linux 870
Motor2B = GPIO("/dev/gpiochip1", 21, "out")
#Motors2E --> 23 #GPIO Linux 867
Motor2E = GPIO("/dev/gpiochip1", 23, "out")


print ("Going forwards")
Motor1A.write(bool(HIGH))
Motor1B.write(bool(LOW))
Motor1E.write(bool(HIGH))

Motor2A.write(bool(HIGH))
Motor2B.write(bool(LOW))
Motor2E.write(bool(HIGH))

sleep(2)
print ("Going backwards")
Motor1A.write(bool(LOW))
Motor1B.write(bool(HIGH))
Motor1E.write(bool(HIGH))

Motor2A.write(bool(LOW))
Motor2B.write(bool(HIGH))
Motor2E.write(bool(HIGH))

sleep(2)
print ("Now stop!")
Motor1E.write(bool(LOW))
Motor2E.write(bool(LOW))

#free
Motor1A.close()
Motor1B.close()
Motor1E.close()
Motor2A.close()
Motor2B.close()
Motor2E.close()

#end
