def transponeeriK(maatriks):
    uusmaatriks=[]
    for a in range(len(maatriks[0])):
        uusmaatriks.append([])
    for rida in maatriks:
        uusveerg=[]
        for el in rida:
            uusveerg.insert(0,el)
        for a in range(len(uusveerg)):
            uusmaatriks[a].insert(0,uusveerg[a])
    return(uusmaatriks)
