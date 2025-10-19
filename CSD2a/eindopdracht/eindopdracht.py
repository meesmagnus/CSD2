#2nd order Markov chain

import random
import time
import pygame
import inputValidation as iv

'''DNA'''
#4 sounds are used: Silence, kick, snare and hihat. This can be expanded upon.
dna = iv.inputValidation("\nPlease provide the sequence DNA: \namount of sounds used, amount of steps in measure, random seed \n(no comma's or brackets. -> Use spaces) \n", "DNA")
soundAmount = dna[0]
measureSize = dna[1]
random.seed(dna[2])

'''Playback'''
BPM = iv.inputValidation("BPM: ", "float", [1, 9999999])
stepSizeSec = (60/BPM)/iv.inputValidation("speed multiplier: ", "float", [1, 9999999])




#First I generate a 3 dimensional lookup table to lookup probability values
#This will be random each time the code is executed.
#To find the probabilities of the sounds to play next, u use your past 2 sounds
#as coordinates like this: pLookup[2nd to last played sound][last played sound].
#This will spit out a list of probability values for the next sound to be played.
def generateLookupTable(soundAmount):
    pLookup = []
    som = []
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
    return pLookup



#a measure always starts with a kick
#to start the Markov Chain, you need previous values,
#but because these are not yet available at the beginning, I start with a kick at index 0
#at index 1, I execute the Markov Chain, but because I cannot look two steps back in time (index -1),
#I use a temporary variable “ignition” instead of index -1, (to refer to a similarity in a car engine)
#Ignition is a random integer.


def markovChain(pLookup, measureSize):
    seq = []
    ignition = random.randint(0, soundAmount - 1)
    seq.insert(0, 1)
    seq.insert(1, random.choices(population = range(soundAmount),weights = pLookup[ignition][seq[0]])[0])
    #Now that the sequence has a basis from which the Markov Chain can be executed,
    #I do this in a loop that starts at i = 2, because the first 2 values are already fixed.
    #I always check whether i is divisible by stepAmtTillReset, because this means the start of a new measure.
    #If so, I insert a kick (that's how you feel the one). If not, I execute the Markov Chain.

    for i in range(2, 8 * measureSize):
        if i % measureSize == 0:
            seq.insert(i, 1)
        else:
            seq.insert(i, random.choices(population = range(soundAmount), weights = pLookup[seq[i-2]][seq[i-1]])[0])
    return seq


#add timestamps
def getTimestamps(seqIn, stepSizeSec):
    seq = []
    for i in range(len(seqIn)):
        seq.append([i*stepSizeSec, seqIn[i]])
    return seq

#make events using dictionary
def makeEvents(seqIn):
    seq = []
    for i in range(len(seqIn)):
            event = {
                "sound": seqIn[i][1],
                "timestamp": seqIn[i][0]
            }
            seq.append(event)
    return seq

#play the sequence
def playSeq(seq, soundAmount):
    pygame.init()
    samples = []
    #make array of playable sounds
    for i in range(soundAmount):
        samples.append(pygame.mixer.Sound('sounds/{}.wav'.format(i)))

    startTime = time.time()
    for event in seq:
        while time.time() - startTime < event['timestamp']:
            time.sleep(0.001)
        pygame.mixer.stop() #choke other sounds
        samples[event['sound']].play()

    time.sleep(1) #let the last note ring out
    playAgain = input("'y' to play again: ")
    if playAgain == 'y':
        playSeq(seq, soundAmount)


#the flow
pLookup = generateLookupTable(soundAmount)

serialSeq = markovChain(pLookup, measureSize)

doubleSerialSeq = serialSeq + serialSeq

timestampedSeq = getTimestamps(doubleSerialSeq, stepSizeSec)

eventsSeq = makeEvents(timestampedSeq)
print(serialSeq) #print simple representation of the sequence
playSeq(eventsSeq, soundAmount)
