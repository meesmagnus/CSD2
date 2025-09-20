#2nd order Markov chain
import random

soundAmount = 3
seq=[]

#generate 3 dimensional lookup table
for i in range(soundAmount): 					    #2nd to last played note
    for j in range(soundAmount): 				    #last played note
        for k in range(soundAmount): 			    #Prob. next sound
            pLookup[i][j][k] = random.randint(0, 100)
									                #make numbers on axis j add up to 1
        sum[j] = sum(array[i][j]) 				    #calculate sum of pLookup[i][j]
        for k in range(soundAmount):
			pLookup[i][j][k] = array[i][j][k]/sum[j]

#als er nog geen basis is waarop de markov chain kan worden gestart,
#append een kick en een 1st order Markov chain met als 2nd order randomness.
if seq.len <= 2:
	seq[0] = 0 						#Kick
    #kies 1,2 of 3 op basis van een weighted random functie, met weights uit de lookup table
    seq[1] = random.choice(range(soundAmount), weight=pLookup[random(range(soundAmount)] [seq[1]] )

for(i=2; 1< 64; i++):                #range nader te bepalen
	seq[i] = random.choice(range(soundAmount), weight=pLookup[seq[i-2]] [seq[i-1]])


print(seq)



#ideas:
#hihat has higher chance of playing double
