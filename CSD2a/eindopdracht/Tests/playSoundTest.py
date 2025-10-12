import time
import pygame


seq = [{'sound': 0, 'timestamp': 0.0}, {'sound': 0, 'timestamp': 0.5}, {'sound': 3, 'timestamp': 1.0}, {'sound': 3, 'timestamp': 1.5}, {'sound': 3, 'timestamp': 2.0}, {'sound': 2, 'timestamp': 2.5}, {'sound': 0, 'timestamp': 3.0}, {'sound': 0, 'timestamp': 3.5}, {'sound': 3, 'timestamp': 4.0}, {'sound': 3, 'timestamp': 4.5}, {'sound': 3, 'timestamp': 5.0}, {'sound': 1, 'timestamp': 5.5}, {'sound': 0, 'timestamp': 6.0}, {'sound': 0, 'timestamp': 6.5}, {'sound': 0, 'timestamp': 7.0}, {'sound': 0, 'timestamp': 7.5}, {'sound': 3, 'timestamp': 8.0}, {'sound': 3, 'timestamp': 8.5}, {'sound': 0, 'timestamp': 9.0}, {'sound': 1, 'timestamp': 9.5}, {'sound': 0, 'timestamp': 10.0}, {'sound': 2, 'timestamp': 10.5}, {'sound': 1, 'timestamp': 11.0}, {'sound': 0, 'timestamp': 11.5}, {'sound': 0, 'timestamp': 12.0}, {'sound': 0, 'timestamp': 12.5}, {'sound': 0, 'timestamp': 13.0}, {'sound': 3, 'timestamp': 13.5}, {'sound': 1, 'timestamp': 14.0}, {'sound': 0, 'timestamp': 14.5}, {'sound': 0, 'timestamp': 15.0}, {'sound': 3, 'timestamp': 15.5}, {'sound': 3, 'timestamp': 16.0}, {'sound': 1, 'timestamp': 16.5}, {'sound': 1, 'timestamp': 17.0}, {'sound': 1, 'timestamp': 17.5}, {'sound': 0, 'timestamp': 18.0}, {'sound': 2, 'timestamp': 18.5}, {'sound': 1, 'timestamp': 19.0}, {'sound': 0, 'timestamp': 19.5}, {'sound': 2, 'timestamp': 20.0}, {'sound': 1, 'timestamp': 20.5}, {'sound': 0, 'timestamp': 21.0}, {'sound': 2, 'timestamp': 21.5}, {'sound': 1, 'timestamp': 22.0}, {'sound': 2, 'timestamp': 22.5}, {'sound': 1, 'timestamp': 23.0}, {'sound': 2, 'timestamp': 23.5}]
soundAmount = 4
samples = []

def playSeq(seq, soundAmount):
    pygame.init()
    for i in range(soundAmount):
        samples.append(pygame.mixer.Sound('../sounds/{}.wav'.format(i)))

    startTime = time.time()
    for event in seq:
        while time.time() - startTime < event['timestamp']:
            time.sleep(0.001)

        samples[event['sound']].play()


playSeq(seq, soundAmount)
