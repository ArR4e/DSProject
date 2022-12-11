

def transponeeriK(tp):
    transponeeritud = []
    transponeerimata = []
    while True:
        parem = []
        for x in tp:
            if len(x) < 1:
                break
            lisatav = x.pop(-1)
            parem.append(lisatav)
        if len(parem) < 1:
            break
        transponeerimata.append(parem)
            
    while True:
        
        for llisatav in transponeerimata:
            vasak = []
            for lllisatav in llisatav:
                vasak.insert(0, lllisatav)
            transponeeritud.append(vasak)
        
        break
    return transponeeritud
            
        
        
    
    


#print(transponeeriK([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
#print(transponeeriK([[1, 2], [3, 4], [5, 6], [7, 8]]))