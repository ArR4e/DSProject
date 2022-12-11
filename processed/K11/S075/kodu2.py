def transponeeriK(maatriks):
    uus=[]
    uusrida=[]
    ridasid=len(maatriks)
    veerge=len(maatriks[0])
    for esimene in range(veerge):
        uusrida.clear()
        for teine in range(ridasid):
            uusrida.append(maatriks[ridasid-1-teine][veerge-1-esimene])
        uus.append(uusrida[:])
    return uus
    
print(transponeeriK([[4, 31, 67, 99]]))