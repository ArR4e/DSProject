def transponeeriK(maatriks):
    
    transponeeritud=[]
    x=[]
    a=0
    
    for i in range(len(maatriks)):
        for j in range(len(maatriks[i])):
            x=x+[maatriks[len(maatriks)-1-i][len(maatriks[i])-j-1]]
    
    for k in range(len(maatriks[a])):
        transponeeritud=transponeeritud+[[x[k]]]
        if len(maatriks)!=1:
            l=k
            while l <= (len(maatriks)+k):
                transponeeritud[k]=transponeeritud[k]+[x[l+len(maatriks[a])]]
                l+=len(maatriks[a])
    return transponeeritud
