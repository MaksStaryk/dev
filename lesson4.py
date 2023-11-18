import math
"""start task 1"""
print('start task 1')
a = -1
b = 21
c = 3

print( a < 0 ,b < 0,c < 0)
print()
"""start task 2"""
print('start task 2')
n = 12
k = 9
if n //2 *2 ==n and k //2 *2 == k:
    print('есть четность')
else:
    print('нет четности')
print()
"""start task 4"""
print('start task 4')
v = '99'
q = int(v[0])
w = int(v[1])
if q + w <10:
    print('Da')
else:
    print('Net')
print('task 5')
a = 10
b = 1
while a <= 29:
    print(b,'раз:', 10,)
    a += 1
    b += 1
print()
''''task 6'''
print('task 6')
some_number_6 = 7
i = 1
while i <=some_number_6:
    print((pow(i,3)), end=' ')
    i +=1
print()
"""start task 9"""
print('start task 9')
a = 96
minimum = 10
while a > 0:
    d = a %  10
    if d < minimum:
        minimum = d
    a //= 10
    print(minimum)
