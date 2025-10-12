#2nd order Markov chain

import random
import time
import pygame

#4 sounds are used: Silence, kick, snare and hihat. This can be expanded upon.

dna = input("\nPlease provide the sequence DNA: \namount of sounds used, amount of steps in measure, random seed: \n(no comma's or brackets. Use spaces) \n").split()
soundAmount = int(dna[0])
measureSize = int(dna[1])
random.seed(dna[2])
BPM = float(input("BPM: "))
stepSizeSec = (60/BPM)/float(input("speed multiplier: "))
pLookup=[]
seqV1=[]
seqV2=[]
seqV3=[]
som=[]




#First I generate a 3 dimensional lookup table to lookup probability values
#This will be random each time the code is executed.
#To find the probabilities of the sounds to play next, u use your past 2 sounds
#as coordinates like this: pLookup[2nd to last played sound][last played sound].
#This will spit out a list of probability values for the next sound to be played.

for i in range(soundAmount):
    pLookup.insert(i, [])
    for j in range(soundAmount):
        pLookup[i].insert(j, [])
        for p in range(soundAmount):
            pLookup[i][j].insert(p, random.randint(0, 100))
#make numbers on axis j add up to 1
        som.insert(j, sum(pLookup[i][j]))
        for p in range(soundAmount):
            pLookup[i][j][p] = pLookup[i][j][p]/som[j]



#a measure always starts with a kick
#to start the Markov Chain, you need previous values,
#but because these are not yet available at the beginning, I start with a kick at index 0
#at index 1, I execute the Markov Chain, but because I cannot look two steps back in time (index -1),
#I use a temporary variable “ignition” instead of index -1, (to refer to a similarity in a car engine)
#Ignition is a random integer.

ignition = random.randint(0, soundAmount - 1)
seqV1.insert(0, 1)
seqV1.insert(1, random.choices(population = range(soundAmount),weights = pLookup[ignition][seqV1[0]])[0])

#Now that the sequence has a basis from which the Markov Chain can be executed,
#I do this in a loop that starts at i = 2, because the first 2 values are already fixed.
#I always check whether i is divisible by stepAmtTillReset, because this means the start of a new measure.
#If so, I insert a kick (that's how you feel the one). If not, I execute the Markov Chain.

def markovChain(seq, pLookup, measureSize):
    for i in range(2, 8 * measureSize):
        if i % measureSize == 0:
            seq.insert(i, 1)
        else:
            seq.insert(i, random.choices(population = range(soundAmount), weights = pLookup[seq[i-2]][seq[i-1]])[0])



#add timestamps
def timestamps(seqIn, seqOut, stepSizeSec):
    for i in range(len(seqIn)):
        seqOut.append([i*stepSizeSec, seqIn[i]])

#make seperate timestamp lists for each sound (not used, because redundant)
def separateSounds(seqIn, seqOut, soundAmount):
    for i in range(soundAmount):
        seqOut.append([])
    for i in range(len(seqIn)):
        seqOut[seqIn[i][1]].append(seqIn[i][0])

#make events using dictionary
def makeEvents(seqIn, seqOut):
    for i in range(len(seqIn)):
            event = {
                "sound": seqIn[i][1],
                "timestamp": seqIn[i][0]
            }
            seqOut.append(event)


def playSeq(seq, soundAmount):
    pygame.init()
    samples = []
    #make array of playable sounds
    for i in range(soundAmount):
        samples.append(pygame.mixer.Sound('sounds/{}.wav'.format(i)))

    startTime = time.time()
    #go through the sequence and play!
    for event in seq:
        while time.time() - startTime < event['timestamp']:
            time.sleep(0.001)
        pygame.mixer.stop()
        samples[event['sound']].play()

    time.sleep(1) #let the last note ring out
    playAgain = input('play again? (y/n)')
    if playAgain == 'y':
        playSeq(seq, soundAmount)





markovChain(seqV1, pLookup, measureSize)
timestamps(seqV1, seqV2, stepSizeSec)
makeEvents(seqV2, seqV3)
print(seqV1)
playSeq(seqV3, soundAmount)
