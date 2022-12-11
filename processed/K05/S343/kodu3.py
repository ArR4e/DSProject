def moos(sk, vk, k):
    kk = 0
    while k - 5 >= 0 and sk > 0:
        k -= 5
        kk += 1
        sk -= 1
        
        if k == 0:
            return kk
        if k < 5 or sk == 0:
            continue
        
    while k - 1 >= 0 and vk > 0:
        k -= 1
        kk += 1
        vk -= 1
        if k == 0:
            return kk
        elif vk == 0:
            return -1
    if k == 0:
        return 0
    else:    
        return -1
             
moos(15, 40, 39)

