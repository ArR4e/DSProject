def transponeeriK(matrix):
    for i in range(len(matrix)):
        matrix[i].reverse()
    matrix.reverse()
    print(matrix)
    zipped_rows = zip(*matrix)
    transposed_matrix = [list(row) for row in zipped_rows]
    return transposed_matrix
    
