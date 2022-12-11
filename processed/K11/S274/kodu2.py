def transponeeriK(maatriks):
    järjend1 = []
    for i in range(len(maatriks[0])-1, -1, -1):
        järjend2 = []
        for j in range(len(maatriks)-1, -1, -1):
            järjend2.append(maatriks[j][i])
        järjend1.append(järjend2)
    return järjend1
