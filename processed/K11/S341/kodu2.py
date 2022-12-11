import numpy as np
from random import randint, sample
def loo_maatriks():
    matrix=[]
    veerud = 3
    read = 3
    for i in range(veerud):
        matrix.append()
    for j in range(read):
        matrix[-1].append(randint(10))
    return matrix
def loo_maatriks():
    read = 3
    return [sample(range(10), read) for _ in range(3)]
matrix = loo_maatriks()
[print(rida) for rida in matrix]
def transponeeriK(matrix):
    m=[]
    m.append(matrix)
    for i in range(2, -1,-1):
        for j in range(1,-1,-1):
            print(m[j][i], end="")
        print()
transponeeriK(matrix)