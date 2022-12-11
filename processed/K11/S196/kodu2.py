from copy import deepcopy

def transponeeriK(maatriks):
    maatriks = maatriks[::-1]
    transponeeritud_maatriks = deepcopy(maatriks)
    print(len(maatriks))
    for rida in range(len(maatriks)):
        for element in range(len(maatriks[0])):
            transponeeritud_maatriks[rida][element] = maatriks[element][rida]
    lõplik_maatriks = transponeeritud_maatriks[::-1]
    return(lõplik_maatriks)
print(transponeeriK([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))