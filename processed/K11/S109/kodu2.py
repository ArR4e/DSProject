def transponeeriK(maatriks):
    jär1 = []
    for i in range(2,-1,-1):
        jär2 = []
        for j in range(1,-1,-1):
            a = (maatriks[j][i])
            jär2.append(a)
        return jär2
    
transponeeriK([[1,2,3],[3,4,5]])