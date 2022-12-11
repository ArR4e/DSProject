def transponeeriK(maatriks):
    read = len(maatriks)
    tulbad = len(maatriks[0])
    
    Maatriks = []
    for i in range(tulbad):
        rida = []
        for j in range(read):
            rida.append(maatriks[j][i])
        Maatriks.append(rida)
        
    return Maatriks

maatriks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transponeeriK(maatriks))