import random
arr = []
som = []
leng = 3

for i in range(leng):
    arr.insert(i, [])
    for j in range(leng):
        arr[i].insert(j, [])
        for k in range(leng):
            arr[i][j].insert(k, random.randint(0, 10))
        for k in range(leng):
            som.insert(k, sum(arr[i][j]))
print(arr)
print(arr[0][0])
print(sum(arr[0][0]))
