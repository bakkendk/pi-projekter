from gpiozero import OutputDevice, MotionSensor
from time import sleep

skrigemaskine = OutputDevice(26, active_high=False, initial_value=False)
monster = OutputDevice(21, active_high=False, initial_value=False)
pir = MotionSensor(4)

numberOfActivations = 0

skrigemaskine.off()
monster.off()
print('Wait 4 seconds before starting')
sleep(4)

while True:
    print('Waiting for movement')
    pir.wait_for_motion()
    print('Motion detected')
    numberOfActivations = numberOfActivations+1
    print('Number of activations:',numberOfActivations)
    skrigemaskine.on()
    sleep(0.2)
    skrigemaskine.off()
    for x in range(70):
        monster.toggle()
        sleep(0.1)
    monster.off()
    print('Force delay 8 seconds')
    sleep(8) #Force x seconds of delay before next cycle
    
    
    

