import random

weights = [0.1, 0.1, 0.8]
# list = [appel, janneke, toon]

randTest = random.choices(population=range(3), weights=weights, k=10)
# print(list(range(3)))
print(randTest)
