import pygame
import time

# init  mixer module
pygame.init()

#this function recieves a value and plays a beep this amount of times
def playBeep(replayAmount):
    sample = pygame.mixer.Sound('./beep.wav')
    i = 0
    while i < replayAmount:
        sample.play()
        time.sleep(sample.get_length())
        i += 1


#user passes value, it is converted to an integer, and is passed to a function
playBeep(int(input("Amount of beeps:")))
