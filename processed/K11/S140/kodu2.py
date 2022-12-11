def transponeeriK(matrix):
    matrix.reverse()
    uusmatrix = []
    
    for i in range(len(matrix[0])):
        uusmatrix.append([])

    for i in range(len(uusmatrix)):
        for j in range(len(matrix)):
            uusmatrix[i].append(matrix[j][i])
    uusmatrix.reverse()
    
    return uusmatrix
