def transponeeriK(origmat):
    
    transmat=[]
    for x in reversed(range(len(origmat[0]))):
        uusrida=[]
        for rida in origmat:
            uusrida.insert(0,rida[x])
        transmat.append(uusrida)
    return(transmat)