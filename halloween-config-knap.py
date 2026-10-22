from gpiozero import LED, Button
from time import sleep

ledZombie = LED(27)
lysKaede = LED(17)
lyd = LED(22)
button = Button(2)

ledZombie.off()
lysKaede.on()
lyd.on()

while True:
    button.wait_for_press()
    lysKaede.off()
    lyd.off()
    for x in range(70):
        ledZombie.toggle()
        sleep(0.1)
    lyd.on()
    ledZombie.off()
    lysKaede.on()
