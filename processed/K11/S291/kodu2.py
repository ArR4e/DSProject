def transponeeriK(maatriks):
    uus_maatriks = []
    for i in range(len(maatriks[0]) - 1, -1, -1):
        järjend = []
        for j in range(len(maatriks) - 1, -1, -1):
            järjend.append(maatriks[j][i])
        uus_maatriks.append(järjend)
    return uus_maatriks
            
    
# print(transponeeriK([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print(transponeeriK([[1, 2], [3, 4], [5, 6], [7, 8]]))
# print(transponeeriK([[4, 31, 67, 99]]))