"""import math
x = float(input("input x = "))
y = float(input("input y = "))
f = (((math.log(x-y)) / (x-y) * (pow(x, 4) + pow(y, 4)) + (4 * pow(x, 2) * pow(y, 2))) * math.log1p(math.sqrt(1 + pow(x, 2) + pow(y, 2))))
print("Answer: ", f)"""


from math import log, sqrt
x = float(input("input x = "))
y = float(input("input y = "))
f = (((log(x-y)) / (x-y) * (x**4 + y**4) + (4 * x**2 * y**2)) * log(sqrt(1 + x**2 + y**2)))
print('Answer: ', f)
