import RPi.GPIO as GPIO
import time

lysSensor = 18
togRelae = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(lysSensor, GPIO.IN)
GPIO.setup(togRelae, GPIO.OUT)

try:
    while True:
        lysSensorValue = GPIO.input(lysSensor)
        if lysSensorValue == GPIO.HIGH:
            GPIO.output(togRelae, GPIO.LOW)
        else:
            GPIO.output(togRelae, GPIO.HIGH)
        time.sleep(0.2)
        
except KeyboardInterrupt:
    print('Program stoppet')
finally:
    GPIO.cleanup()
