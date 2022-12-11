def transponeeriK(m):
    rida = len(m)
    veerg = len(m[0])
    
    m2 = []
    
    for i in range(veerg):
        m2.append([])
        for el in range(rida):
            m2[i].append(m[rida-el-1][veerg-i-1])
            
    
    return m2
