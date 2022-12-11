
def transponeeriK (maatriks):
    m = []          
    for i in range(len(maatriks[0])-1, -1, -1):
        r = []
        for j in range(len(maatriks)-1, -1, -1):
            r.append(maatriks[j][i])
        m.append(r)            
    return m

