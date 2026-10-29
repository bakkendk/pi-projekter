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
    print('Number of activations: ',numberOfActivations)
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
    print('Force delay')
    sleep(8) #Force x seconds of delay before next cycle
