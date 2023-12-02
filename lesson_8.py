"""task 7"""
stroka = "backer"

try:
    print(stroka[10])
except IndexError:
    print('net takogo indexa. repeat')
print()
"""task 8"""
def delit(a:int,b ="str"):
    return a/b
try:
    print(delit(4))
except TypeError:
    print('зачем делить на строку!!!!!!')
print()
"""task 10"""
lst = [1,3,4]

try:
    num = int(input('your index:'))
    lst.remove(num)
except ValueError:
    raise TypeError('net takogo elementa')