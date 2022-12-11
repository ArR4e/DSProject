with open(input("Sisesta failinimi: "), encoding= "utf-8") as f:
    read = []
    for rida in f:
        read.append(rida.strip().split())
    ajad = []
    
    for i in range(0, len(read)):
        a = read[i][0].split(":")
        b = read[i][1].split(":")
        ajad.append([(int(a[0])*60 + int(a[1])), int(b[0])*60 + int(b[1]), int(read[i][2])])
    
    s = 0
    for i in range(len(read)-1):
        for j in range(2):
            if ajad[i][0] - ajad[i+1][0] < ajad[i][1] - ajad[i+1][1] and ajad[i][2] > ajad[i+1][2]:
                read.remove(read[i-s])
                s += 1
                
                
    for i in range(len(read)-1):
        for j in range(0, len(ajad)-i-1):
            if read[j][0] > read[j+1][0]:
                read[j], read[j + 1] = read[j + 1], read[j]
                
    print(" Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
    for el in read:
        print(el[0], el[1], el[2])