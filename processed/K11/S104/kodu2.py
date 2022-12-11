import numpy as np
def transponeeriK(maatriks):
    matrix = np.arrey(maatriks)
    matrix = matrix[::-1]
    matrix = matrix.transpose()
    matrix = matrix[::-1]
    return matrix.tolist()

print(transponeeriK([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))