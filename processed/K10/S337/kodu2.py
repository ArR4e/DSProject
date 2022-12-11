def võitja(maatriks):
    i = 0
    j = 0
    n_x = 0
    n_o = 0
    for rida in maatriks:
        for veerg in rida:
            if veerg =='X':
                n_x += järjest(i, j, maatriks)
            elif veerg =='O':
                n_o += järjest(i, j, maatriks)
            j+=1
        j = 0
        i +=1
    return {'O': n_o, 'X': n_x}
def järjest(i, j, maatriks): #kontroll, kas leidub järjestikku olevaid elemente
    n = 1
    vastus = 0
    x = j+1
    while True: # veergude kaupa
        try:
            if maatriks[i][j] == maatriks[i][x]:
                n +=1
                if n ==3:
                    vastus +=1
                    break
                x +=1
            else:
                break
        except:
            break
    x = i + 1
    n = 1
    while True: #ridade kaupa
        try:
            if maatriks[i][j] == maatriks[x][j]:
                n += 1
                if n == 3:
                    vastus += 1
                    break
                x += 1
            else:
                break
        except:
            break
    y = j+1
    x = i+1
    n = 1
    while True: #diagonaal alla paremale
        try:
            if maatriks[i][j] == maatriks[x][y]:
                n+=1
                if n == 3:
                    vastus +=1
                    break
                x += 1
                y += 1
            else:
                break
        except:
            break
    y = j-1
    x=i+1
    n = 1
    while True: # diagonaal alla vasakule
        try:
            if maatriks[i][j] == maatriks[x][y]:
                n += 1
                if n == 3:
                    vastus +=1
                    break
                x += 1
                y -= 1
                if y < 0:
                    break
            else:
                break
        except:
            break
    return vastus
