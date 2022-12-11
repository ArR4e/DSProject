def transponeeriK(m):
    m.reverse()
    for rida in m:
        rida.reverse()
    
    uuedread = []
    for r in range(len(m[0])):
        uuedread.append([])
    for a in range(len(m)):
        for i in range(len(m[a])):
            uuedread[i].append(m[a][i])
    return(uuedread)
         
print(transponeeriK([[1,2,3],
                [4,5,6],
                [7,8,9]]))