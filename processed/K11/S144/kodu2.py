maatriks = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]

def transponeeriK(m):
    vahe_m = []
    uus_m = []
    for i in range(len(m[0])-1,-1,-1):
        for j in range(len(m)-1,-1,-1):
                vahe_m.append(m[j][i])
        uus_m.append(vahe_m)
        vahe_m = []
    return uus_m
    
print(transponeeriK(maatriks))