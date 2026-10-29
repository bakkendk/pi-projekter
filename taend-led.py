from gpiozero import LED
from picozero import pico_led
from time import sleep


led = LED(26)

led.on()
pico_led.on()
sleep(1)
pico_led.off()
led.off()

