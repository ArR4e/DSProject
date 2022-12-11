def võitja(maatriks):
    sümbolite_arv = {"O" : 0, "X" : 0}
    for i in range(len(maatriks)):
        for j in range(len(maatriks)):
            if maatriks[i][j] in "OX":
                if j < 2 and maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2]: #horisontaalselt
                    sümbolite_arv[maatriks[i][j]] += 1
                if i < 2 and maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j]: #vertikaalselt
                    sümbolite_arv[maatriks[i][j]] += 1
                if i < 2 and j < 2 and maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2]: #diagonaalis paremale
                    sümbolite_arv[maatriks[i][j]] += 1
                if i < 2 and j > 1 and maatriks[i][j] == maatriks[i+1][j-1] == maatriks[i+2][j-2]: # diagonaalis vasakule
                    sümbolite_arv[maatriks[i][j]] += 1
    return sümbolite_arv