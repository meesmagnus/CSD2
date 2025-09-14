import time
import pygame

#define step time in milliseconds
ms = 60000/120      #60000 divided by bpm

dur = [2, 3, 4, 1, 2, 2, 3, 4, 8, 2]
#durms = [i * ms for i in dur]       #multiply list by scalar ms

pygame.init()                       #init sound engine
sample = pygame.mixer.Sound('./beep.wav')   #define sound


for i in dur:               #play beeps over dur
    sample.play()
    print(dur[i])
    time.sleep(dur[i]*(ms/1000))
