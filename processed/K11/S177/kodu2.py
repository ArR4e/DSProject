import numpy as np

def transponeeriK (maatriks):
    transponeeritud_maatriks = maatriks.transpose()
    õige = transponeeritud_maatriks[::-1]
    return õige

maatriks = np.array ([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(transponeeriK(maatriks))

#numpy ilmselt ei tohi kasutada, aga ilma ei suutnud lõpuni teha :((

# def transponeeriK(maatriks):
#     pea_diagonaali_järgi = [[maatriks[j][i] for j in range(len(maatriks))] for i in range(len(maatriks[0]))]
#     for rida in pea_diagonaali_järgi:
#         algne = rida[::-1]
#     print(algne)
#         
    
    
maatriks = [[1, 2],
            [3, 4],
            [5, 6],
            [7, 8]]

# transponeeriK(maatriks)