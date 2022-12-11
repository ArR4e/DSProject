def seosta_lapsed_ja_vanemad(x, y):
    sõnastik1 = {}
    sõnastik2 = {}
    j = []
    f = open(x, encoding="UTF-8")
    f2 = open(y, encoding="UTF-8")
    for rida in f2:
        r = rida.strip("\n").split(" ")
        sõnastik1[r[0]] = r[1] +" "+r[2]
    for rida3 in f:
        r3 = rida3.strip("\n").split(" ")
        j.append(r3[0])
        j.append(r3[1])
    for i in range(len(j)):
        if j[i] in sõnastik1:
            j[i] = sõnastik1[j[i]]
    for el in range(1, len(j), 2):
        if j[el] in sõnastik2:
            sõnastik2[j[el]] = {sõnastik2[j[el]], j[el-1]}            
        else:
            sõnastik2[j[el]] = j[el-1]
    f.close()
    f2.close()
    return(sõnastik2)

s = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
o = []

    

    
    
