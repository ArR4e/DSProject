def transponeeriK(maatriks):
    
    uus=[]
    rida=[]
    # esimene tsükkel annab alamjärjendi el. indeksi
    for i in range(-1,-(len(maatriks[0])+1),-1):
        #teine tsükkel annab järjendi maatriksis
        for j in range(-1,-(len(maatriks)+1),-1):
            rida.append(maatriks[j][i])
        uus.insert(-i,rida[:])
        rida.clear()
        
    return uus

