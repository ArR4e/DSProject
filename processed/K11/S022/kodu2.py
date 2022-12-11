"""import math
import copy
def transponeeriK(maatriks):
    maatriks1 = maatriks
    maatriks2 = maatriks
    koopia = copy.deepcopy(maatriks)
    kuljepikkus = len(maatriks)
    for kulg in range(kuljepikkus):
        for kulg2 in range(kuljepikkus):
            maatriks2[kuljepikkus - 1 - kulg2][kuljepikkus - 1 - kulg] = koopia[kulg][kulg2]
    return(maatriks2)
    
transponeeriK([[1, 2, 3], [4, 5, 6], [7, 8, 9]])"""

import math
import copy
import numpy as np

def transponeeriK(maatriks):
    maatriks2 = maatriks
    koopia = copy.deepcopy(maatriks)
    kuljepikkus1 = len(maatriks)
    kuljepikkus2 = len(maatriks[0])
    a = []
    maatriks = np.random.randint(0, 1, size=(kuljepikkus2,kuljepikkus1))
    for kulg in range(kuljepikkus1):
        for kulg2 in range(kuljepikkus2):
            maatriks[kuljepikkus2 - 1 - kulg2][kuljepikkus1 - 1 - kulg] = koopia[kulg][kulg2]
    
    for element in maatriks:
        element = list(element)
    #maatriks = list(maatriks)
    #maatriks = maatriks.replace(" ",", ")
    # maatriks = list(maatriks)
    maatriks = maatriks.tolist()
    return(maatriks)


transponeeriK([[1, 2], [3, 4], [5, 6], [7, 8]])