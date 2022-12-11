def transponeeriK(maatriks):
    read = len(maatriks)
    veerud = len(maatriks[0])
    print("r=", read)
    print("v=", veerud)
    uus_maatriks = [[0 for i in range(read)] for j in range(veerud)]
    #print(uus_maatriks)
    for rida in range(0, veerud):
        print("rida=", rida)
        for veerg in range(0, read):
            print(rida, "x", veerg, "->", read - 1 - veerg, "x", veerud - 1 - rida, "=", maatriks[read - veerg - 1][veerud - 1 - rida])
            uus_maatriks[rida][veerg] = maatriks[read - veerg - 1][veerud - 1 - rida]
            
    return uus_maatriks
    
    
    
print(transponeeriK([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]))

print(transponeeriK([[1, 2],
                     [3, 4],
                     [5, 6],
                     [7, 8]]))

print(transponeeriK([[4, 31, 67, 99]]))

print(transponeeriK([[11, 12, 13, 14, 15, 16, 17, 18, 19],
                     [21, 22, 23, 24, 25, 26, 27, 28, 29],
                     [31, 32, 33, 34, 35, 36, 37, 38, 39]]))
