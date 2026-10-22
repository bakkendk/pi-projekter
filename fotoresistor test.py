import RPi.GPIO as GPIO
from gpiozero import LED
import time

GPIO.setmode(GPIO.BCM)
photo_pin = 18
relay = LED(17)

GPIO.setup(photo_pin, GPIO.IN)

try:
    while True:
        if GPIO.input(photo_pin) == GPIO.HIGH:
            #print("Der er lys - stop toget!")
            relay.on()
        else:
            #print("Der er ikke lys - kør tog!")
            relay.off()
        time.sleep(0.2)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
    