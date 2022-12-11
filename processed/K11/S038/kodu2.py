

def transponeeriK(matrix):
    a = []
    for i in range(len(matrix[0]) -1,-1,-1):
        b = []
        for n in range(len(matrix) -1,-1,-1):
            b.append(matrix[n][i])
        a.append(b)
    return a
