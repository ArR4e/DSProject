def transponeeriK(matrix):
    if len(matrix) == 1:
        matrix[0].reverse()
        return [[i] for i in matrix[0]]
    
    [i.reverse() for i in matrix]
    matrix = [i for i in matrix[::-1]]
    temp_matrix = [[] for i in range(len(matrix[0]))]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            temp_matrix[j].append(matrix[i][j])
    return temp_matrix
