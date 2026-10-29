from gpiozero import OutputDevice
from time import sleep
import pygame


#relay1 = OutputDevice(26)
relay = OutputDevice(6)
servo = OutputDevice(26)
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=8192)
pygame.mixer.music.load('/home/bakke/Scripts/Ring02.wav')

while True:
    #relay3.on()
    print('Send signal')
    servo.on()
    sleep(0.1)
    servo.off()
    pygame.mixer.music.play()
    sleep(4)
    relay.toggle()
    sleep(4)
