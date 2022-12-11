def transponeeriK(x):
    uus=[]
    o=len(x)
    for i in range(len(x)):
        veeluuem=[]
        for j in range(len(x)):
            veeluuem.append(x[o-i-1][o-j-1])
        uus.insert(i,veeluuem)
    return uus
