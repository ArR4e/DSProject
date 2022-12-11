def võitja(maatriks):
    tagasta = {}
    O = 0
    X = 0
    for rida in range(len(maatriks)):
        x_rida = 0
        o_rida = 0
        x_veerg = 0
        o_veerg = 0
        for veerg in range(len(maatriks[rida])):
            if maatriks[rida][veerg] == 'X':
                x_rida += 1
                if x_rida >= 3:
                    X += 1
            else:
                x_rida = 0
            if maatriks[veerg][rida] == 'X':
                x_veerg += 1
                if x_veerg >= 3:
                    X += 1
            else:
                x_veerg = 0
            if maatriks[rida][veerg] == 'O':
                o_rida += 1
                if o_rida >= 3:
                    O += 1
            else:
                o_rida = 0
            if maatriks[veerg][rida] == 'O':
                o_veerg += 1
                if o_veerg >= 3:
                    O += 1
            else:
                o_veerg = 0
    tagasta['O'] = O
    tagasta['X'] = X
    return tagasta