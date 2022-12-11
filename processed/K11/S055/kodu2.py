def transponeeriK(m):
    m.reverse()
    uus_m = []
    for i in range(-1, -len(m[0])-1, -1):
        uus_m.append([rida[i] for rida in m])
    return uus_m
        
print(transponeeriK([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(transponeeriK([[1, 2], [3, 4], [5, 6], [7, 8]]))
print(transponeeriK([[4, 31, 67, 99]]))
