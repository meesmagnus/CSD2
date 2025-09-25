#2nd order Markov chain
import random
#4 geluiden: kick, snare, hihat en stilte
soundAmount = 4
seq=[]
pLookup=[]
som=[]

#generate 3 dimensional lookup table
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

# als er nog geen basis is waarop de markov chain kan worden gestart,
# append een kick en een 1st order Markov chain met als 2nd order randomness.

# print(pLookup[0][0])

#kick
seq.insert(0, 0)


#kies 1,2 of 3 op basis van een weighted random functie, met weights uit de lookup table
kickstart = random.randint(0, soundAmount - 1)
# weights = pLookup[kickstart][seq[0]]

seq.insert(1, random.choices(population = range(soundAmount),weights = pLookup[kickstart][seq[0]])[0])

#range nader te bepalen
for i in range(2, 64):
    seq.insert(i, random.choices(population = range(soundAmount), weights = pLookup[seq[i-2]][seq[i-1]])[0])


print(seq)



#ideas:
#hihat has higher chance of playing double
#hoe initialiseer ik een 3 dimensionale array?
#array methods insert

# [1,2,3,4,5,6]
#
# pLookup[i] = [[][]]
