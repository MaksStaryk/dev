year = int(input('enter a year:'))

if ( year % 4 ==0 and year % 100 !=0) or year % 400 ==0:
    print('год  високосный')
else:
    print('год не високосный')