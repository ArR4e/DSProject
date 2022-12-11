import numpy as np
def transponeeriK(matrixx):
    return np.matrix.transpose(np.array(matrixx[::-1])).tolist()[::-1]