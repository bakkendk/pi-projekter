from gpiozero import OutputDevice
from time import sleep

# Definér de fire spoler (GPIO-numre)
coil_A = OutputDevice(17)
coil_B = OutputDevice(23)
coil_C = OutputDevice(27)
coil_D = OutputDevice(22)

# Half-step sekvens (8 trin)
sequence = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1],
]

coils = [coil_A, coil_B, coil_C, coil_D]

def step(steps, delay=0.002, direction=1):
    idx = 0
    for _ in range(steps):
        for coil, value in zip(coils, sequence[idx]):
            if value:
                coil.on()
            else:
                coil.off()
        idx = (idx + direction) % len(sequence)
        sleep(delay)

# Eksempel: én omdrejning frem og tilbage
try:
    print("Frem")
    step(4096, delay=0.001, direction=1)  # ca. 0,5 omdrejning
    sleep(1)
    print("Tilbage")
    step(16384, delay=0.001, direction=-1)
finally:
    for c in coils:
        c.off()