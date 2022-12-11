def transponeeriK(maatriks):
    transponeeritud=[]
    for kord in range(len(maatriks[0])):
        transponeeritud.append([])
    for i in range(len(maatriks)):
        a=0
        for j in range(len(maatriks[len(maatriks)-1-i])):
            a+=1
            if len((maatriks[len(maatriks)-1-i]))>=j:
                transponeeritud[len(transponeeritud)-a].append((maatriks[len(maatriks)-1-i])[j])
            else:
                continue      
    return(transponeeritud)
transponeeriK([[1, 2], [3, 4], [5, 6], [7, 8]])
          

            