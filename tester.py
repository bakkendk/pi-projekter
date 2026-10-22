from gpiozero import LED
from time import sleep

led = LED(22)


led.off()


while True:
    for x in range(65):
        led.toggle()

        sleep(0.5)
    led.off()