def transponeeriK(maatrix):
    read = len(maatrix) -1
    try:
        veerud = len(maatrix[0]) -1
    except:
        return []
    uuslist = []

    if read == veerud:
        for i in range(read,-1,-1):
            uusmaatrix = []
            for j in range(veerud,-1,-1):
                uusmaatrix.append(maatrix[j][i])
            uuslist.append(uusmaatrix)
    else:
        for j in range(veerud,-1,-1):
            uusmaatrix = []
            for i in range(read,-1,-1):
                uusmaatrix.append(maatrix[i][j])
            uuslist.append(uusmaatrix) 
        
    return uuslist

maatrix = [
            [2,1,-1],
            [7,1,3]
            ]

print(transponeeriK(maatrix))
