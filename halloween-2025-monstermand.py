from gpiozero import OutputDevice, MotionSensor
from time import sleep


skrigemaskine = OutputDevice(26, active_high=False, initial_value=False)
#relay2 = OutputDevice(20, active_high=False, initial_value=False)
monster = OutputDevice(21, active_high=False, initial_value=False)
pir = MotionSensor(4)

numberOfActivations = 0

skrigemaskine.off()
monster.off()
sleep(4)

while True:
    print('Waiting for movement')
    pir.wait_for_motion()
    print('Motion detected')
    numberOfActivations = numberOfActivations+1
    print('Number of activations:',numberOfActivations)
    skrigemaskine.on()
    sleep(0.1)
    skrigemaskine.off()
    for x in range(70):
        monster.toggle()
        sleep(0.1)
    monster.off()
    print('Check if movement stopped')
    motion_stopped = False
    for y in range(10): #Check 50 times for 0.1 mili seconds
        if not pir.motion_detected:
            motion_stopped = True
            break
        sleep(0.1)
    if motion_stopped:
        print('Movement stopped')
        skrigemaskine.off()
        monster.off()
    else:
        print('Movement still registered')
    print('Force delay')
    sleep(8) #Force x seconds of delay before next cycle
    
    
    

