def seosta_lapsed_ja_vanemad(lapsed, nimed):
    f_lapsed = open(lapsed).readlines()
    f_nimed = open(nimed).readlines()
    seotud = {}
    for i in f_lapsed:
        i = i.split()
        for j in f_nimed:
            j = j.split()
            j[1:] = [" ".join(j[1:])]
            if i[1] == j[0]:
                for x in f_nimed:
                    x = x.split()
                    x[1:] = [" ".join(x[1:])]
                    if i[0] == x[0]:
                        if j[1] in seotud:
                            a = seotud[j[1]]
                            t = set()
                            t.add(a)
                            t.add(x[1])
                            seotud[j[1]] = t
                        else:
                            seotud[j[1]] = x[1]
    for i in seotud:
        print(i, end = ": ")
        if len(seotud[i]) == 2:
            for x,j in enumerate(seotud[i]):
                if x != 1:
                    print(j, end = ", ")
                else:
                    print(j)
        else:
            print(seotud[i])
    return seotud
                