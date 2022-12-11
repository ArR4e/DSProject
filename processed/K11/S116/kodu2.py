def transponeeriK(maatriks):
    vaherida = []
    uusmaatriks = []
    for j in range(len(maatriks[0])):
        for i in range(len(maatriks)):
            vaherida.append(maatriks[-i-1][-j-1])
        uusmaatriks.append(vaherida)
        vaherida = []
            
    
            
    return uusmaatriks

maatriks = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(transponeeriK(maatriks))

