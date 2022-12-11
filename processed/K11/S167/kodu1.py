def seosta_lapsed_ja_vanemad(failinimi_lapsed, failinimi_nimed):
    f1 = open(failinimi_lapsed, "r")
    f2 = open(failinimi_nimed, "r")

    list1 = []
    for i in f1:
        vanem_ja_laps = i.strip().split()
        list1.append(vanem_ja_laps)

    list2 = []
    for i in f2:
        isikukood_ja_vanem = i.strip().split()
        list2.append(isikukood_ja_vanem)

    for i in range(0, len(list2)):
        list2[i] += " "
        list2[i][2], list2[i][3] = list2[i][3], list2[i][2]
        list2[i][1] = list2[i][1] + list2[i][2] + list2[i][3]
        list2[i].pop(2), list2[i].pop(2) 



    lapsed = []
    i = 0
    while i<len(list1):
        if list1[i][1] not in lapsed:
            lapsed.append(list1[i][1])
        i += 1
    sõnastik1 = {}
    for l in lapsed:
        v = []
        for i in list1:
            if l in i[1]:
                v.append(i[0])
        
        sõnastik1[l] = v


    sõnastik = {}
    arv = 0
    for i in sõnastik1.keys():
        for i2 in list2:
            if i == i2[0]:
                laps = i2[1]

        vanem = set()
        for i2 in sõnastik1[i]:
            for i3 in list2:
                if i2 in i3[0]:
                    vanem.add(i3[1])
        sõnastik[laps] = vanem
        arv += 1
    return sõnastik
#print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))
