def year(a):
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        print("Високосный")
    else:
        print("Невисокосный")

for a in range(2000, 2010, 1):
 year(a)
        