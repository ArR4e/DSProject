def transponeeriK(maatriks):
    uus_1,uus_2 = [],[]
    for b in range(len(maatriks[0])):
        uus_1 = []
        for a  in range(len(maatriks)):
            uus_1 += [maatriks[a][b]]
        uus_2 +=[uus_1]
    uus_3,uus_4 = [],[]
    for a in range (len(uus_2)):
        uus_3 = []
        for b in range (len(uus_2[a])):
            uus_3+=[uus_2[-a-1+len(uus_2)][-1-b+len(uus_2[a])]]
        uus_4+=[uus_3]
    return uus_4