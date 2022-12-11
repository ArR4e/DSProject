def transponeeriK(m):
    a=len(m)-1
    b=len(m[0])-1
    n=[]
    for i in range(b+1):
            n.append([0]*(a+1))
    for x in range(len(m)):
        for y in range(len(m[x])):
            n[y][x]=m[a-x][b-y]
    return n
print(transponeeriK([[1, 2], [3, 4], [5, 6], [7, 8]]))