import numpy as np

def massive(a):
    ''' Перемножение элементов массива 
    определенного библиотекой Numpy
    '''
    b = 1
    for i in range(0, len(a), 1):
        b = b*a[i]
        
    return b

print(massive(np.array([2, 3, 4])))