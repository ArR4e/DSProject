def seosta_lapsed_ja_vanemad(fail1, fail2):
    f2 = open(fail2)
    isikutesõnastik = {}
    for rida in f2:
        rida = (rida.strip("\n")).split()
        isikutesõnastik[rida[0]] = rida[1] + " " + rida[2]
    f2.close()
    f1 = open(fail1)
    sõnastik = {}
    for rida in f1:
        rida = (rida.strip("\n")).split()
        laps = isikutesõnastik[rida[1]]
        vanem = isikutesõnastik[rida[0]]
        if laps not in sõnastik:
            sõnastik[laps] = set()
        if vanem not in sõnastik[laps]:
            sõnastik[laps].add(vanem)
    f1.close()
    return sõnastik

vastus = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
for võti in vastus:
    print(võti, end = ": ")
    if len(vastus[võti]) == 2:
       nimed = ", ".join(str(s) for s in vastus[võti])
       print(nimed)
    else:
        print(str(vastus[võti]).strip("{'").strip("'}"))
