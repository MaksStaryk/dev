import math
"""start task 9"""
print('start task 9')
a = 15678123
minimum = 10
while a:
    d = a %  10
    if d < minimum:
        minimum = d
    a //= 10
print(minimum)
