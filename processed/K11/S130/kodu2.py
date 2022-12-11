

def transponeeriK(maatriks):
    s = len(maatriks) -1
    o = len(maatriks[0]) -1
    uus = []
    for i in range(o, -1, -1):
        esimene = []
        for j in range(s, -1, -1):
            esimene.append(maatriks[j][i])
        uus.append(esimene)
    return uus
    
    
    
    
print(transponeeriK([[1,2,3],
                     [4,5,6],
                     [7,8,9]]))