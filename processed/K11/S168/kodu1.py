def seosta_lapsed_ja_vanemad(laste_fail, nimede_fail):
    tehtud_dict = {}
    f1 = open(laste_fail, encoding = 'utf-8')
    isikukoodide_d = {}
    for rida in f1:
        rida = rida.strip().split()
        if rida[1] not in isikukoodide_d:
            isikukoodide_d[rida[1]] = list()
            isikukoodide_d[rida[1]].append(rida[0])
        else:
            isikukoodide_d[rida[1]].append(rida[0])
    f1.close()

    f2 = open(nimede_fail, encoding = 'utf-8')
    nimede_isikukoodid = {}
    for rida in f2:
        rida = rida.strip().split()
        nimi = rida[1] + ' ' + rida[2]
        nimede_isikukoodid[rida[0]] = nimi
    f2.close()
    
    for key in isikukoodide_d:
        for i in range(len(isikukoodide_d[key])):
            if i == 0:
                nimed = set()
                nimi = nimede_isikukoodid[isikukoodide_d[key][i]]
                nimed.add(nimi)
            else:
                nimi = nimede_isikukoodid[isikukoodide_d[key][i]]
                nimed.add(nimi)
        tehtud_dict[nimede_isikukoodid[key]] = nimed
    return tehtud_dict

dict = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")

for key in dict:
    vanemad = ''
    for i in range(len(dict[key])):
        vanemad += list(dict[key])[i]
        if i != len(dict[key]) - 1:
            vanemad += ', '
    print(key + ': ' + vanemad)
    
    