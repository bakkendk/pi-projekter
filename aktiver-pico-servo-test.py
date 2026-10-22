from gpiozero import LED
from time import sleep

led = LED(23)

led.on()
print('Taend')
sleep(0.2)
print('Sluk')
led.off()
