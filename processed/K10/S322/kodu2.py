
def võitja(tabel):
    # loo sõnastik, sea vaikeväärtused
    mängjad = {}
    mängjad["X"] = 0
    mängjad["O"] = 0
    kõrgus = len(tabel)
    laius = len(tabel[0])
    for rida in tabel:
        # kontrolli reas esinemiste arvu
        if rida.count("X") >= 3:
            mängjad["X"] += 1
        elif rida.count("O") >= 3:
            mängjad["O"] += 1
    for i in range(laius):
        # kontrolli veerus esinemiste arvu
        veerg = []
        for rida in tabel:
            veerg += [rida[i]]
        if veerg.count("X") >= 3:
            mängjad["X"] += 1
        elif veerg.count("O") >= 3:
            mängjad["O"] += 1
    # kontrollime kahte diagonaali erinevatest suundadest,
    # vastasel korral tekiksid kattuvused
    for t in range(2):
        for nihe_y in range(kõrgus):
            for nihe_x in range(laius):
                diagonaal = []
                x = nihe_x
                y = nihe_y
                if t == 1:
                    while x < laius and y > -1:
                        diagonaal += [tabel[y][x]]
                        x += 1
                        y -= 1
                else:
                    while x > -1 and y > -1:
                        diagonaal += [tabel[y][x]]
                        x -= 1
                        y -= 1
                if len(diagonaal) >= 3:
                    if diagonaal.count("X") >= 3:
                        mängjad["X"] += 1
                    elif diagonaal.count("O") >= 3:
                        mängjad["O"] += 1
    # tagasta
    return mängjad
