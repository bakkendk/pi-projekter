from gpiozero import Servo
from time import sleep

# Brug GPIO 17 (pin 11)
SERVO_PIN = 18

# For mange servoer passer dette område cirka.
# min_pulse_width og max_pulse_width kan justeres.
servo = Servo(SERVO_PIN, min_pulse_width=0.0005, max_pulse_width=0.0025)

print("Bevæger servo fra max til min...")

try:
    while True:
        # Maksimum (ca. 180 grader)
        servo.max()
        print("Maks position")
        sleep(1)

        # Minimum (ca. 0 grader)
        servo.min()
        print("Min position")
        sleep(1)

        # Midterposition
        servo.mid()
        print("Midt position")
        sleep(1)

except KeyboardInterrupt:
    print("Stopper servo...")
