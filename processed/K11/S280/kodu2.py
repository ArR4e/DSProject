# 2. Maatriksi transponeerimine kõrvaldiagonaali järgi / RP

def transponeeriK(maatriks):
    transponeeritud = []
    for i in range(len(maatriks[0])):
        stack = []
        for x in range(len(maatriks)):
            stack.append(maatriks[(len(maatriks)-1)-x][(len(maatriks[0])-1)-i])
        transponeeritud.append(stack)
    return transponeeritud
    
print(transponeeriK([[1, 2], [3, 4], [5, 6], [7, 8]]))