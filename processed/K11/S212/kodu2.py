def transponeeriK(maatriks):
    transponeeritud = []
    for i in range(len(maatriks[0])):
        transponeeritud.append([])
        for j in range(len(maatriks)):
            transponeeritud[i].append(maatriks[len(maatriks)-j-1][len(maatriks[0])-i-1])
    return transponeeritud
print(transponeeriK([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
             