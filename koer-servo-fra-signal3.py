import RPi.GPIO as GPIO
from gpiozero import Servo
from time import sleep

pin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)
SERVO_PIN = 18
servo = Servo(SERVO_PIN, min_pulse_width=0.0005, max_pulse_width=0.0025)


servo.min()
print("Venter på signal...")
while True:
    if GPIO.input(pin):
        print("Signal modtaget!")
        servo.max()
        print("Maks position")
        sleep(4)
        servo.min()
        print("Min position")
