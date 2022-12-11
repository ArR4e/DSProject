def transponeeriK(maatriks):
    vastus = []
    for elem in maatriks[0]:
        vastus += [[""]]
    for rida in range(len(maatriks)-1):
        for i in range(len(vastus)):
            vastus[i] += [""]
            print(vastus[i])
            
    for i in range(len(maatriks)):
        for j in range(len(maatriks[i])):
            vastus[len(maatriks[i])-1-j][len(maatriks)-1-i] = maatriks[i][j]
    return vastus
print(transponeeriK([[7, 7, 5],
                     [9, 6, 3],
                     [7, 5, 8]]))