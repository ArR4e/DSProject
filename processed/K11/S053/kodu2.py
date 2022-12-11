def transponeeriK(maatriks):
    transponeeritud_kuju = []
    veerg = len(maatriks[0]) - 1
    rida = len(maatriks) - 1

    for i in range(veerg, -1, -1):
        järjend = []
        for j in range(rida, -1, -1):
            järjend.append(maatriks[j][i])        
        transponeeritud_kuju.append(järjend)
        
    return transponeeritud_kuju

transponeeriK([[1, 2], [3, 4], [5, 6], [7, 8]])