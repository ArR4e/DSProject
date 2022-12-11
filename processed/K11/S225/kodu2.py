def transponeeriK(maatriks):
    a = []
    for i in range(len(maatriks[0])-1,-1,-1):
        #veerud
        b=[]
        for j in range(len(maatriks)-1,-1,-1):
            #read
            b.append(maatriks[j][i])
        a.append(b)
    return a
