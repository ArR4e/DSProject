def transponeeriK(m):
    vahepealne = []
    for a in range(len(m)):
        vahepealne.append(m[a])
        #print(m[a])
    vahepealne.reverse()
    #print(vahepealne)
    uus = []
    for a in range(len(vahepealne[0])):
        uus.append([])
    kordaja = 0
    a = 0
    while True:
    
        uus[kordaja].append(vahepealne[a][-1])
        vahepealne[a].remove(vahepealne[a][-1])
        #print(vahepealne)
        #uus[a]
        a+=1
        if a == len(m):
            a = 0
        if len(uus[-1]) == len(m):
            break
        #uus[kordaja].append(vahepealne[a][-1])
        if len(uus[kordaja]) == len(m):
            kordaja += 1
    return(uus)







#maatriks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transponeeriK([[1, 2, 3], [4, 5, 6], [7, 8, 9]])