def transponeeriK(maatriks):
    uus_maatriks = []
    veerge = 0
    for element in maatriks[0]:
        veerge += 1
    for i in range(veerge-1,-1,-1):
        lisa_järjend = []
        for j in range(len(maatriks)-1,-1,-1):
            lisa_järjend+=[maatriks[j][i]]
        uus_maatriks += [lisa_järjend]
    return uus_maatriks
