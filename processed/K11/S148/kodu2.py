# kõrvaldiagonaali suhtes
def transponeeriK(a):
    
    veerud = len(a[0])
    aT = veerud * [[]]
    
    i = 0
    while 0 < veerud:
        read = len(a)
        r = []
        while 0 < read:
            r += [a[read - 1][veerud - 1]]
            read -= 1
        aT[i] = r
        veerud -= 1
        i += 1
    
    return aT

"""
# peadiagonaali suhtes
def transponeeriK(a):
    read = len(a)
    veerud = len(a[0])
    
    aT = veerud * [[]]
    
    i = 0
    while i < veerud:
        j = 0
        r = []
        while j < read:
            r += [a[j][i]]
            j += 1
        aT[i] = r
        i += 1
    
    return aT
"""