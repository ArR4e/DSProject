# import numpy as np
def transponeeriK(maatriks):
    read=len(maatriks)
    veerud=len(maatriks[0])
    maatriks2=[]
    for i in range(veerud,0,-1):
        rida=[]
        for j in range(read,0,-1):
            rida.append(maatriks[j-1][i-1])
        maatriks2.append(rida)
    return maatriks2
         
# def transponeeriK(a):
#     x=np.rot90(np.fliplr(a),-1)
#     return x