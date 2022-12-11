# 1. Lapsed ja vanemad  
def seosta_lapsed_ja_vanemad(lastefailinimi, nimedefailinimi):
    fail2 = open(nimedefailinimi)
    isikud = {}
    for rida in fail2:
        rida = (rida.strip("\n")).split()
        isikud[rida[0]] = rida[1] + " " + rida[2]
    fail2.close()
    
    fail1 = open(lastefailinimi)
    sõnastik = {}
    for rida in fail1:
        rida = (rida.strip("\n")).split()
        laps = isikud[rida[1]]
        vanem = isikud[rida[0]]
        if laps not in sõnastik:
            sõnastik[laps] = set()
        if vanem not in sõnastik[laps]:
            sõnastik[laps].add(vanem)
    fail1.close()
    return sõnastik

tulemus = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
for võti in tulemus:
    print(võti, end = ": ")
    if len(tulemus[võti]) == 2:
        nimed = ", ".join(str(s) for s in tulemus[võti])
        print(nimed)
    else:
        print(str(tulemus[võti]).strip("{'").strip("'}"))