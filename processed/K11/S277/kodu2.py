import numpy as np
import ast
maatriks = input('Sisestage maatriks: ')
maatriks = ast.literal_eval(maatriks)

def transponeeriK(maatriks):
    maatriks = np.transpose(np.array(maatriks))
    maatriks = np.flip(maatriks)
    return maatriks
