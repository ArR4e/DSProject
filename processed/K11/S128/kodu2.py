#Maatriksi transponeerimine kõrvaldiagonaali järgi

def transponeeriK(maatriks):
    y = len(maatriks)
    x = len(maatriks[0])
    transponeeritud = [[0]*y for i in range(x)]
    for j in range(y-1, -1, -1):
        for i in range(x-1, -1, -1):
            k = abs(i-(x-1))
            m = abs(j-(y-1))
            transponeeritud[k][m] = maatriks[j][i]
            
    return transponeeritud

print(transponeeriK([[1, 2], [3, 4], [5, 6], [7, 8]]))