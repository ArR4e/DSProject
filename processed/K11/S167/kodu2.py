#maatriksi transpondeerimine

#vahetada diagonaalide järgi eelneva näit vastandnäiduga
#m = [[11, 12, 13, 14, 15], [21, 22, 23, 24, 25], [31, 32, 33, 34, 35], [41, 42, 43, 44, 45], [51, 52, 53, 54, 55]]
#m = [[1,2], [3, 4], [5,6], [7, 8]]
def transponeeriK(m):
    t = []

    for i in range(len(m[0])-1, -1, -1):
        list = []
        for j in range(len(m)-1, -1, -1):
            list.append(m[j][i])
        t.append(list)
    return t

#print(t)