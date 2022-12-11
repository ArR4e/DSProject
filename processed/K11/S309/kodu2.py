def transponeeriK(matrix):

    result = []
    for j in range(len(matrix[0])-1,-1,-1):
        column = []
        for i in range(len(matrix)-1,-1,-1):
                column.append(matrix[i][j])
        result.append(column)
    
    return result