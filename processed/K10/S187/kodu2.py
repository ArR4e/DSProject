def võitja(ruudustik):
    tulemus = {'O': 0, 'X': 0}

    # teen veerud
    veerud = []
    for i in range(len(ruudustik[0])):
        veerg = []
        for rida in ruudustik:
            veerg.append(rida[i])
        veerud.append(veerg)

    # teen diagonaalid
    diagonaalid = [
        [ruudustik[0][0], ruudustik[1][1], ruudustik[2][2], ruudustik[3][3]],
        [ruudustik[0][3], ruudustik[1][2], ruudustik[2][1], ruudustik[3][0]],
        [ruudustik[0][2], ruudustik[1][1], ruudustik[2][0]],
        [ruudustik[1][3], ruudustik[2][2], ruudustik[3][1]],
        [ruudustik[0][1], ruudustik[1][2], ruudustik[2][3]],
        [ruudustik[1][0], ruudustik[2][1], ruudustik[3][2]]
    ]

    # horisontaalselt
    for rida in ruudustik:
        for i  in range(len(rida)):
            if rida[i] != ' ':
                try:
                    if rida[i - 1] == rida[i] and rida[i - 2] == rida[i]:
                        tulemus[rida[i]] += 1
                except:
                    pass
    
    # vertikaalselt
    for veerg in veerud:
        for i  in range(len(veerg)):
            if veerg[i] != ' ':
                try:
                    if veerg[i - 1] == veerg[i] and veerg[i - 2] == veerg[i]:
                        tulemus[veerg[i]] += 1
                except:
                    pass

    # diagonaalselt
    for dia in diagonaalid:
        for i in range(len(dia)):
            if dia[i] != ' ':
                try:
                    if dia[i - 1] == dia[i] and dia[i - 2] == dia[i]:
                        tulemus[dia[i]] += 1
                except:
                    pass

    return(tulemus)

'''    for i in range(len(ruudustik)):
        rida = ruudustik[i]
        for j in range(len(rida)):
            if rida[j] != ' ':
                try:
                    if ruudustik[i - 1][j - 1] == rida[j] and ruudustik[i - 2][j - 2] == rida[j]:
                        tulemus[rida[j]] += 1
                    if ruudustik[i - 1][j + 1] == rida[j] and ruudustik[i - 2][j + 2] == rida[j]:
                        tulemus[rida[j]] += 1
                except:
                    pass
'''