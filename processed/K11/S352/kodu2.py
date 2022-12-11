def transponeeriK(maatriks):
    transponeeritud=[]
    for i in range(len(maatriks[0])-1,-1,-1):
        rida=[]
        for y in reversed(maatriks):
            rida.append(y[i])    
        transponeeritud.append(rida)
    return transponeeritud
