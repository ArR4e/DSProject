import numpy as np

def transponeeriK(maatriks):
    b = np.array(maatriks)
    a = b[::-1,::-1].T
    return(a.tolist())