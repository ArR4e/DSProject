import numpy as np

m=([[1,2,3],[4,5,6],[7,8,9]])

def transponeeriK(m):
    m2=np.fliplr(m)
    m2=m2.transpose()
    m2=np.fliplr(m2)
    m3=m2.tolist()
    return(m3)
print(transponeeriK(m))