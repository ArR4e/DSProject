def transponeeriK(maatriks):
    trans = []
    
    for i in range(len(maatriks[0]) -1, -1, -1):
        el = []
    for j in range(len(maatriks[0]) -1, -1, -1):
        el += [maatriks[i][j]]
    trans += el
    
    return trans

print(transponeeriK([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        
        

        
        