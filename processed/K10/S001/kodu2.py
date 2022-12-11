def võitja(maatriks):
    o = 0
    x = 0
    for rida in range(len(maatriks)):
        for koht in range(len(maatriks[rida])):
            if koht <= 1 and maatriks[rida][koht]==maatriks[rida][koht+1] and maatriks[rida][koht]==maatriks[rida][koht+2]:
                if maatriks[rida][koht] == "O":
                    o += 1
                elif maatriks[rida][koht] == "X":
                    x += 1
            if rida <= 1 and maatriks[rida][koht]==maatriks[rida+1][koht] and maatriks[rida][koht]==maatriks[rida+2][koht]:
                if maatriks[rida][koht] == "O":
                    o += 1
                elif maatriks[rida][koht] == "X":
                    x += 1
            if rida <= 1 and koht <= 1 and maatriks[rida][koht]==maatriks[rida+1][koht+1] and maatriks[rida][koht]==maatriks[rida+2][koht+2]:
                if maatriks[rida][koht] == "O":
                    o += 1
                elif maatriks[rida][koht] == "X":
                    x += 1
            if rida >= 2 and koht <= 1 and maatriks[rida][koht]==maatriks[rida-1][koht+1] and maatriks[rida][koht]==maatriks[rida-2][koht+2]:
                if maatriks[rida][koht] == "O":
                    o += 1
                elif maatriks[rida][koht] == "X":
                    x += 1
    return {"O": o, "X": x}
