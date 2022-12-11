def transponeeriK(x):
    b,a = len(x[0]), len(x)
    maatriks = [[0 for x in range(a)] for y in range(b)] 
    
    for i in range(len(x)):
        for j in range(len(x[0])):
            maatriks[j][i]=x[len(x)-1-i][len(x[0])-1-j]
            
    return maatriks