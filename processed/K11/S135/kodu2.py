def transponeeriK(matrix):
    transMatrix = []
    for i in range(len(matrix[0])):
        line = [0] * len(matrix)
        for j in range(len(matrix)):
            line[j] = matrix[(j + 1) * -1][(i + 1) * -1]
        transMatrix += [line]
    return transMatrix