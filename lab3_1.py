from random import randint

arr = [randint(1,20) for _ in range(30)]

sum1 = sum(arr[0:10])
sum2 = sum(arr[10:20])
sum3 = sum(arr[20:30])

print('Arr:', arr)
if sum1 < sum2 and sum1 < sum3:
    print('First decade less than others. Sum is:', sum1)

if sum2 < sum1 and sum2 < sum3:
    print('Second decade less than others. Sum is:',sum2)

if sum1 > sum3 < sum2:
    print('Third decade less than others. Sum is:',sum3)

if sum(arr[0:15]) > sum(arr[15: 30]):
    print('First half more than second')
else:
    print('Second half more than first')