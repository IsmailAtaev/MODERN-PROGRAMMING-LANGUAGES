from random import randint
import numpy as np

arr = [[randint(1,100) for _ in range(10)] for _ in range(10)]
diog = []
result = []

for i in range(10):
    diog.append(arr[i][i])

for i in range(10):
    counter = 0
    for j in range(10):
        if arr[j][i] < diog[i]:
            counter += 1

    result.append(counter)

print('Matrix:', np.matrix(arr), '\n')
print('Elem of diagonal:', diog)
print('Result:', result)

