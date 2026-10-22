from gpiozero import Servo
from gpiozero import Button
from time import sleep

# Servo på GPIO 18 (pin 12)
SERVO_PIN = 18

# Inputsignal fra anden Pi på GPIO 21 (pin 40)
TRIGGER_PIN = 26

# Opret servo- og input-objekter
servo = Servo(SERVO_PIN, min_pulse_width=0.0005, max_pulse_width=0.0025)
trigger = Button(TRIGGER_PIN, pull_up=False)  # pull_down aktiveret

print("Venter på signal... (Ctrl+C for at stoppe)")

try:
    while True:
        if trigger.is_pressed:  # HØJT signal fra den anden Pi
            print("Signal modtaget – kører servo!")
            servo.max()
            print("Maks position")
            sleep(5)

            servo.min()
            print("Min position")
            sleep(5)

        sleep(0.1)  # lille pause for at undgå CPU-belastning

except KeyboardInterrupt:
    print("Stopper servo...")
