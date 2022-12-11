def transponeeriK(maatriks):
    transponeeritud_maatriks = []
    ridade_arv = len(maatriks)
    veergude_arv = 0
    for el in maatriks[0]:
        veergude_arv +=1
            
    for j in range(1,veergude_arv+1):
        järjend = []
        for i in range(1,ridade_arv+1):
            järjend.append(maatriks[-i][-j])
        transponeeritud_maatriks.append(järjend)
    
    return transponeeritud_maatriks