import numpy as np
def transponeeriK(maatriks):
    matrix = np.array(maatriks) #loob maatriksi
    
    matrix = matrix[::-1] #pöörab maatriksi peapeale -> peadiagonaal on endine kõrvaldiagonaal
    matrix = matrix.transpose() #transponeerib maatriksi
    matrix = matrix[::-1] #pöörnab peapeale pööratud ja transponeeritud maatriksi pea peale
    #kuna transponeerimisel oli elementide järjekord vale => peale transponeerimist peab veerud õigesse järjekorda seadma
    return matrix.tolist()
