def transponeeriK(maatriks):
    transponeeri_maatriks = []
    for i in range(len(maatriks[0])):
        transpor = []
        for j in range(len(maatriks)):
            transpor.append(maatriks[j][i])
        transponeeri_maatriks.append(transpor)
            
    return transponeeri_maatriks
            
            
    
    
    
    
print(transponeeriK([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(transponeeriK([[1, 2], [3, 4], [5, 6], [7, 8]]))

