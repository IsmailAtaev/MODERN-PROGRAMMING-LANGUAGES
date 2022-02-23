import math
x = float(input("input x = "))
y = float(input("input y = "))
f = (((math.log(x-y)) / (x-y) * (pow(x, 4) + pow(y, 4)) + (4 * pow(x, 2) * pow(y, 2))) * math.log1p(math.sqrt(1 + pow(x, 2) + pow(y, 2))))
print(f)
