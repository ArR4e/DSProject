def transponeeriK(maatriks):
    matrix = []
    rida = []
    for i in range(len(maatriks[0])-1, -1, -1):
        rea = []
        for j in range(len(maatriks)-1, -1, -1):
            rea += [maatriks[j][i]]
        matrix += [rea]
    return matrix

    
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
print(transponeeriK([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))