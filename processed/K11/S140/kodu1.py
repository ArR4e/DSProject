def seosta_lapsed_ja_vanemad(i, j):
    f = open(j, encoding="utf-8")
    isik = {}
    for rida in f:
        rida = rida.strip().split()
        isik[rida[0]] = " ".join(rida[1:])
        
    f.close()

    f = open(i, encoding="utf-8")
    sõnastik = {}
    for rida in f:
        rida = rida.strip().split()
        laps = isik[rida[1]]
        vanem = isik[rida[0]]
        if laps not in sõnastik:
            sõnastik[laps] = set()
        sõnastik[laps].add(vanem)
        
    f.close()
    return sõnastik

sõnastik = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")

for võti, väärtus in sõnastik.items():
    väärtus = ", ".join(väärtus)
    print(f"{võti}: {väärtus}")
