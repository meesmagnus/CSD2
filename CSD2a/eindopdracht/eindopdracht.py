#2nd order Markov chain

import random
#4 sounds are used: Kick, snare, hihat and silence. This can be expanded upon.
soundAmount = 4
pLookup=[]
seq=[]
som=[]
stepAmtTillReset = int(input("Step Amount till reset?:"))

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
#I use a temporary variable “ignition” instead of index -1.
#Ignition is a random integer.

ignition = random.randint(0, soundAmount - 1)
seq.insert(0, 0)
seq.insert(1, random.choices(population = range(soundAmount),weights = pLookup[ignition][seq[0]])[0])

#Now that the sequence has a basis from which the Markov Chain can be executed,
#I do this in a loop that starts at i = 2, because the first 2 values are already fixed.
#I always check whether i is divisible by stepAmtTillReset, because this means the start of a new measure.
#If so, I insert a kick (that's how you feel the one). If not, I execute the Markov Chain.

for i in range(2, 8 * stepAmtTillReset):
    if i%stepAmtTillReset == 0:
        seq.insert(i, 0)
    else:
        seq.insert(i, random.choices(population = range(soundAmount), weights = pLookup[seq[i-2]][seq[i-1]])[0])


print(seq)
