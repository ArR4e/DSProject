def transponeeriK(maatriks):
    uus_maatriks = []
    for i in maatriks[0]:
        uus_maatriks.append([])
    for järjend in range(len(maatriks)):
        for element in range(len(maatriks[järjend])):
            uus_maatriks[element].append(maatriks[len(maatriks)-1-järjend][len(maatriks[järjend])-1-element])
            
    return uus_maatriks
