def transponeeriK(list1):
    
    translist = []
    matrix = []

    for j in range(len(list1[0])-1, -1, -1):
        lisatav = []
        for i in range(len(list1)-1, -1, -1):
            lisatav += [list1[i][j]]
        matrix += [lisatav]
                
    return matrix
    
    
    
    
    
    
    
    
    
print(transponeeriK([[4,31,67,99]]))