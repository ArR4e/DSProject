maatrik =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def transponeeriK(maatriks):
    tmaatriks = []
    veerge = len(maatriks[0])
    ridu = len(maatriks)
    for i in range(0, veerge, -1):
        read = []
        tmaatriks.append(read)
        read.clear()
        for j in range(0, ridu, -1):
            read.append(maatriks[j][i])
    return (tmaatriks)
         
print(transponeeriK([[1,2,3],[3,4,5]]))
            