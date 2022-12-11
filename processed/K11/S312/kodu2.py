def transponeeriK(matrix):
    read = []
    ridu = len(matrix)
    veergusid = len(matrix[0])
    for i in range(veergusid-1, -1, -1):
        elemendid = []
        for j in range(ridu-1, -1, -1):
            elemendid.append(matrix[j][i])
        read.append(elemendid)     
    return read        
    
    

