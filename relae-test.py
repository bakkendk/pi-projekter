from gpiozero import OutputDevice
from time import sleep


relay1 = OutputDevice(26, active_high=False, initial_value=False)
relay2 = OutputDevice(20, active_high=False, initial_value=False)
relay3 = OutputDevice(21, active_high=False, initial_value=False)


relay1.off()
relay2.off()
relay3.off()

sleep(4)

while True:
    #relay1.off()
    sleep(0.1)
    #relay1.on()
    relay2.off()
    sleep(0.1)
    relay2.on()
    #relay3.off()
    sleep(0.1)
    #relay3.on()
    sleep(3)