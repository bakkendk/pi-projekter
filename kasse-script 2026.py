from gpiozero import OutputDevice, MotionSensor
from time import sleep

lampe = OutputDevice(26, active_high=False, initial_value=False)
kranium = OutputDevice(20, active_high=False, initial_value=False)
blaeser = OutputDevice(21, active_high=False, initial_value=False)
pir = MotionSensor(4)

print("Script startet. Venter 4 sekunder.")
kranium.off()
blaeser.off()
lampe.off()
sleep(4)
numberOfActivations = 0

while True:
    print('Waiting for movement')
    pir.wait_for_motion()
    print('Motion detected')
    numberOfActivations = numberOfActivations+1
    print('Number of activations:',numberOfActivations)
    
    blaeser.on()
    sleep(0.5)
    kranium.on()
    for i in range(60):
        lampe.toggle()
        sleep(0.1)
    lampe.off()
    sleep(15.5)
    blaeser.off()
    kranium.off()
    print('Check if movement stopped')
    motion_stopped = False
    for y in range(10): #Check 50 times for 0.1 mili seconds
        if not pir.motion_detected:
            motion_stopped = True
            break
        sleep(0.1)
    if motion_stopped:
        print('Movement stopped')
        blaeser.off()
        kranium.off()
    else:
        print('Movement still registered')
    print('Force delay')
    sleep(15) #Force x seconds of delay before next cycle
