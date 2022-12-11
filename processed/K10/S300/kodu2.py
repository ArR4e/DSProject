def võitja(maatriks):
    def horisontaalselt(sümbol):
        arv1 = 0
        arv2 = 0
        for rida in maatriks:
            if rida[0] == sümbol and rida[1] == sümbol and rida[2] == sümbol:
                arv1 += 1
            if rida[1] == sümbol and rida[2] == sümbol and rida[3] == sümbol:
                arv2 += 1
        return arv1 + arv2
    
    def vertikaalselt(sümbol, arv):
        järjend1 = []
        arv1 = 0
        arv2 = 0
        for rida in maatriks:
            järjend2 = []
            indeks = -1
            for element in rida:
                if element == sümbol:
                    indeks += 1
                    järjend2.append(indeks)
                else:
                    indeks += 1
            järjend1.append(järjend2)
        if arv in järjend1[0] and arv in järjend1[1] and arv in järjend1[2]:
            arv1 = 1
        if arv in järjend1[1] and arv in järjend1[2] and arv in järjend1[3]:
            arv2 = 1
        return arv1 + arv2
    
    def diagonaalis1(sümbol, rida, veerg):
        if maatriks[rida][veerg] == maatriks[rida + 1][veerg + 1] == maatriks[rida + 2][veerg + 2] == sümbol:
            arv = 1
        else:
            arv = 0
        return arv
    def diagonaalis2(sümbol, rida, veerg):
        if maatriks[rida][veerg] == maatriks[rida + 1][veerg - 1] == maatriks[rida + 2][veerg - 2] == sümbol:
            arv = 1
        else:
            arv = 0
        return arv
    
    X_horisontaalselt = horisontaalselt("X")
    O_horisontaalselt = horisontaalselt("O")
    X_vertikaalselt = vertikaalselt("X", 0) + vertikaalselt("X", 1) + vertikaalselt("X", 2) + vertikaalselt("X", 3)
    O_vertikaalselt = vertikaalselt("O", 0) + vertikaalselt("O", 1) + vertikaalselt("O", 2) + vertikaalselt("O", 3)
    X_diagonaalis1 = diagonaalis1("X", 0, 0) + diagonaalis1("X", 0, 1) + diagonaalis1("X", 1, 0) + diagonaalis1("X", 1, 1)
    X_diagonaalis2 = diagonaalis2("X", 0, 2) + diagonaalis2("X", 1, 3) + diagonaalis2("X", 0, 3) + diagonaalis2("X", 1, 2)
    O_diagonaalis1 = diagonaalis1("O", 0, 0) + diagonaalis1("O", 0, 1) + diagonaalis1("O", 1, 0) + diagonaalis1("O", 1, 1)
    O_diagonaalis2 = diagonaalis2("O", 0, 2) + diagonaalis2("O", 1, 3) + diagonaalis2("O", 0, 3) + diagonaalis2("O", 1, 2)
    X_mängija = X_horisontaalselt + X_vertikaalselt + X_diagonaalis1 + X_diagonaalis2
    O_mängija = O_horisontaalselt + O_vertikaalselt + O_diagonaalis1 + O_diagonaalis2
    
    sõnastik = {}
    sõnastik["O"] = O_mängija
    sõnastik["X"] = X_mängija
    return sõnastik