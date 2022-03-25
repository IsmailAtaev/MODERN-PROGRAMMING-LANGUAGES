import random
import numpy as np

max_num = 0
index_of_list = None
result = []
arr = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]


def my_func(my_list: list):
    count = 0
    for i in my_list:
        temp = 0
        value = str(i)
        for j in value:
            temp += int(j)
        if temp % 2 == 0:
            count += 1
    return count


for l in arr:
    result.append(my_func(list(l)))

for index, k in enumerate(result):
    if k > max_num:
        max_num = k
        index_of_list = index

print('Matrix:''\n', np.matrix(arr), '\n')
print(arr[index_of_list], max_num)
