def transponeeriK(m):
    uusm = []
    for i in range(len(m)):
        uus = []
        for j in range(len(m[i])):
            if i == j:
                uus += [m[-(i+1)][-(j+1)]]
            elif i != j:
                uus += [m[-(i+1)][-(j+1)]]
        uusm.append(uus)
    return uusm
    
m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[1, 2], [3, 4], [5, 6], [7, 8]]
m3 = [[4, 31, 67, 99]]

print(transponeeriK(m2))