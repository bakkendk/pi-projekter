from gpiozero import LED, MotionSensor
from time import sleep

ledZombie = LED(27)
lysKaede = LED(17)
lyd = LED(22)
pir = MotionSensor(4)

ledZombie.on()
lysKaede.on()
lyd.on()

numberOfActivations = 0

while True:
    print('Waiting for movement')
    pir.wait_for_motion()
    print('Motion detected')
    numberOfActivations = numberOfActivations+1
    print('Number of activations:',numberOfActivations)
    lysKaede.off()
    lyd.off()
    for x in range(70):
        ledZombie.toggle()
        sleep(0.1)
    lyd.on()
    ledZombie.on()
    lysKaede.on()

    print('Check if movement stopped')
    motion_stopped = False
    for y in range(10): #Check 50 times for 0.1 mili seconds
        if not pir.motion_detected:
            motion_stopped = True
            break
        sleep(0.1)

    if motion_stopped:
        print('Movement stopped')
        lyd.on()
        ledZombie.on()
        lysKaede.on()
    else:
        print('Movement still registered')

    print('Force delay')
    sleep(10) #Force x seconds of delay before next cycle