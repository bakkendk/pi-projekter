from gpiozero import Servo
from time import sleep
from gpiozero import Button

# Brug GPIO 17 (pin 11)
SERVO_PIN = 18
# Inputsignal fra anden Pi på GPIO 21 (pin 40)
TRIGGER_PIN = 16

# min_pulse_width og max_pulse_width kan justeres.
servo = Servo(SERVO_PIN, min_pulse_width=0.0005, max_pulse_width=0.0025)
trigger = Button(TRIGGER_PIN, pull_up=False)  # pull_down aktiveret

print("Bevæger servo fra max til min...")

try:
    while True:
        if trigger.is_pressed:  # HØJT signal fra den anden Pi
            # Maksimum (ca. 180 grader)
            servo.max()
            print("Maks position")
            sleep(5)

            # Minimum (ca. 0 grader)
            servo.min()
            print("Min position")
            sleep(5)

except KeyboardInterrupt:
    print("Stopper servo...")

