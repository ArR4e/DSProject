def tee_sõnastikuks(sõne):
    järjend = sõne.split('\n')
    sõnastik = {}
    for element in järjend:
        paarike = element.split(' ', 1)
        sõnastik[paarike[0]] = paarike[1]
    return sõnastik

def seosta_lapsed_ja_vanemad(sõne1, sõne2):
    f_lapsed = open(sõne1, encoding="UTF-8")
    f_nimed = open(sõne2, encoding="UTF-8")
    failist_lapsed = f_lapsed.read().strip()
    failist_nimed = f_nimed.read().strip()
    seosed = failist_lapsed.split()
    isikukoodid = tee_sõnastikuks(failist_nimed)
    f_lapsed.close()
    f_nimed.close()
    
    lapsed = {}
    for indeks in range(0, len(seosed), 2):
        lapse_nimi = isikukoodid[seosed[indeks+1]]
        vanema_nimi = isikukoodid[seosed[indeks]]
        if lapse_nimi not in lapsed:
            lapsed[lapse_nimi] = set()
        lapsed[lapse_nimi].add(vanema_nimi)
    return lapsed

vastus = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
for võti, väärtused in vastus.items():
    i = 0
    for j in väärtused:
        if i == 0:
            print(f"{võti}: {j}", end="")
        else:
            print(f", {j}", end="")
        i += 1
    print()