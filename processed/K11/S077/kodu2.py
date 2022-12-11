def transponeeriK(maatriks):
    uus=[]
    for i in range(len(maatriks[0])):
        uus.append([])
    for x in range(len(uus)):
        for y in range(len(maatriks)):
            uus[x].append(maatriks[-y-1][-x-1])           
    return uus