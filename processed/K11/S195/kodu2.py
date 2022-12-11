def transponeeriK(x):
    uusmat = []
    
    for i in range(len(x[0])-1,-1,-1):
        temp = []
        for j in range(len(x)-1,-1,-1):
            temp.append(x[j][i])
        uusmat.append(temp)
    return uusmat
            

