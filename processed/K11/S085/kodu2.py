def transponeeriK(maatriks):
    järjend = []
    veerg = len(maatriks[0]) - 1
    rida = len(maatriks) -1
    for i in range(veerg,-1,-1):
        järjend2 = []
        for j in range(rida,-1,-1):
            järjend2.append(maatriks[j][i])
        järjend.append(järjend2)
    return järjend
