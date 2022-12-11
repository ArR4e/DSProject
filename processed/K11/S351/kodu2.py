import numpy 
def transponeeriK(maatriks):
    maatriks.reverse()
    for rida in maatriks:
        rida.reverse()
    arr=numpy.array(maatriks)
    transponeeritud=numpy.transpose(arr)
    vastus = transponeeritud.tolist()
    return vastus
    
    
print(transponeeriK([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))