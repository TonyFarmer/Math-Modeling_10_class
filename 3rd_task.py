year = 2100
if year%4 == 0 and year%400 == 0 or year%100 !=0:
    print('Високосный')
else:
    print('Невисокосный')
