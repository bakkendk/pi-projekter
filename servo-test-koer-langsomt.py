from gpiozero import Servo
from time import sleep
import numpy as np

servo = Servo(18)

def smooth_move(start, end, steps=50, delay=0.001):
    values = np.linspace(start, end, steps)  # trin fra start til slut
    for v in values:
        servo.value = v
        sleep(delay)

try:
    while True:
        print("Bevæger fra -1 (venstre) til 1 (højre)")
        smooth_move(-1, 1, steps=100, delay=0.01)
        sleep(1)
        print("Bevæger tilbage fra 1 til -1")
        smooth_move(1, -1, steps=100, delay=0.01)
        sleep(1)

except KeyboardInterrupt:
    print("Stopper")

