def transponeeriK(maatriks):


    uus = []

    read = len(maatriks)
    for i in maatriks:
        veerud = len(i)

    for i in range(veerud-1,-1,-1):
        rida = []
        for j in range(read-1,-1,-1):
            
            element = maatriks[j][i]
            rida.append(element)
            
        
        uus.append(rida)
    return uus

maatriks = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(transponeeriK(maatriks))