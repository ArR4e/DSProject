def transponeeriK(maatriks):
    uus_järjend = []
    for i in range(len(maatriks)-1, -1, -1):
        lisa_järjend = []
        for j in range(len(maatriks[i])-1, -1, -1):
            lisa_järjend += [maatriks[i][j]]
        uus_järjend += [lisa_järjend]
            
    return uus_järjend

print(transponeeriK(([[1, 2], [3, 4], [5, 6], [7, 8]])))