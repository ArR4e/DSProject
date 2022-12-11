import numpy as np
maatriks = ([[4, 31],[2,6],[3,5],[8,7]])

#https://www.askpython.com/python/array/reverse-an-array-in-python
#https://www.geeksforgeeks.org/how-to-reverse-column-order-in-a-matrix-with-python/

def transponeeriK(x):
    #lisasin redigeerimislehelt juurde!
    uus = []
    #flipime ymber, et saaks korvaldiagonaaliga teha 
    x = np.fliplr(x)
    
    #transponeeritud maatriks
    t_x = zip(*x)
    for rida in t_x:
        rida = rida[::-1]
        uus.append(rida)
    return uus
        
x = transponeeriK(maatriks)

