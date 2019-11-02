
def YourDay(day, month, year):
    ''' День(1-31), месяц(1-12), год(от 1582)
    '''
    a = (14 - month) // 12
    year = year - a
    month = month + 12 * a - 2
    return ((day + (31 * month) // 12 + year + year // 4 - year // 100 + year // 400) % 7)
print(YourDay(1, 11, 2019))

