import RPi.GPIO as GPIO
import time

# Opsæt GPIO
GPIO.setmode(GPIO.BCM)
photo_pin = 18
GPIO.setup(photo_pin, GPIO.OUT)
GPIO.output(photo_pin, GPIO.LOW)
time.sleep(0.1)

# Skift til input for at måle opladningstid
GPIO.setup(photo_pin, GPIO.IN)

# Mål opladningstid
def rc_time(photo_pin):
    count = 0
    while (GPIO.input(photo_pin) == GPIO.LOW):
        count += 1
    return count


try:
    while True:
        light_level = rc_time(photo_pin)
        print("Lysniveau: {}".format(light_level))
        if light_level < 10:  # Juster denne værdi efter behov
            print("Lys registreret! Stop toget.")
            # Send kommando til motorcontroller for at stoppe toget
            # fx motor_controller.stop()
        else:
            print("Intet lys - Kør tog!")
        time.sleep(0.5)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()