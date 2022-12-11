def võitja(maatriks):
    sõnastik = {}
    X_arv = 0
    O_arv = 0
    for veerg in range(4):
        for element in range(2):
            if maatriks[veerg][element] == 'X':
                if maatriks[veerg][element]==maatriks[veerg][element+1]==maatriks[veerg][element+2]:
                    X_arv += 1
            elif maatriks[veerg][element] == 'O':
                if maatriks[veerg][element]==maatriks[veerg][element+1]==maatriks[veerg][element+2]:
                    O_arv += 1
    for veerg in range(2):
        for element in range(4):
            if maatriks[veerg][element] == 'X':
                if maatriks[veerg][element]==maatriks[veerg+1][element]==maatriks[veerg+2][element]:
                    X_arv += 1
            elif maatriks[veerg][element] == 'O':
                if maatriks[veerg][element]==maatriks[veerg+1][element]==maatriks[veerg+2][element]:
                    O_arv += 1
    for veerg in range(2):
        for element in range(2):
            if maatriks[veerg][element] == 'X':
                if maatriks[veerg][element]==maatriks[veerg+1][element+1]==maatriks[veerg+2][element+2]:
                     X_arv += 1
            elif maatriks[veerg][element] == 'O':
                if maatriks[veerg][element]==maatriks[veerg+1][element+1]==maatriks[veerg+2][element+2]:
                    O_arv += 1
    for veerg in range(2):
        for element in range(2):
            if maatriks[veerg+2][element] == 'X':
                if maatriks[veerg+2][element]==maatriks[veerg+1][element+1]==maatriks[veerg][element++2]:
                     X_arv += 1
            elif maatriks[veerg+2][element] == 'O':
                if maatriks[veerg+2][element]==maatriks[veerg+1][element+1]==maatriks[veerg][element++2]:
                    O_arv += 1
    sõnastik['O'] = O_arv
    sõnastik['X'] = X_arv
    return sõnastik