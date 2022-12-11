import numpy as np
def transponeeriK(jär):
    jär.reverse()
    for rida in jär:
        rida.reverse()
    arr = np.array(jär)
    transponeeritud = arr.transpose()
    järjend = transponeeritud.tolist()
    return järjend
    