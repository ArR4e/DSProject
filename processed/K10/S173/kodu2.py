def võitja(seis):
    tagastus = {"O":0, "X":0}
    for ls in seis:
        v = 1
        v2 = 2
        for el in range(4):
            if seis.index(ls) == 3:
                v = 0
                v2 = 0
            if el == 2:
                v2 = 1
#horisontaal
            if ls[el] == "O":
                if el + 1 <= 3 and ls[el + 1] == "O":
                    if el + 2 <= 3 and ls[el + 2] == "O":
                        tagastus["O"] += 1
            if ls[el] == "X":
                if el + 1 <= 3 and ls[el + 1] == "X":
                    if el + 2 <= 3 and ls[el + 2] == "X":
                        tagastus["X"] += 1
#vertikaal
            if ls[el] == "O":
                if el + 1 <= 3 and seis[el + 1][el] == "O":
                    if el + 2 <= 3 and seis[el + 2][el] == "O":
                        tagastus["O"] += 1
            if ls[el] == "X":
                if el + 1 <= 3 and seis[el + 1][el] == "X":
                    if el + 2 <= 3 and seis[el + 2][el] == "X":
                        tagastus["X"] += 1
        
#diagonaal
            if ls[el] == "O":
                if el - 1 >= 0:
                    if seis[seis.index(ls) + v][el - 1] == "O":
                        if el - 2 >= 0 and seis[seis.index(ls) + v2][el - 2] == "O":
                            tagastus["O"] += 1
            if ls[el] == "O":
                if el + 1 <= 3:
                    if seis[seis.index(ls) + v][el + 1] == "O":
                        if el + 2 <= 3 and seis[seis.index(ls) + v2][el + 2] == "O":
                            tagastus["O"] += 1
            if ls[el] == "X":
                if el - 1 >= 0:
                    print(seis.index(ls) + v)
                    if seis[seis.index(ls) + v][el - 1] == "X":
                        if el - 2 >= 0 and seis[seis.index(ls) + v2][el - 2] == "X":
                            tagastus["X"] += 1
            if ls[el] == "X":
                if el + 1 <= 3:
                    if seis[el + v][el + 1] == "X":
                        if el + 2 <= 3 and seis[el + v2][el + 2] == "X":
                            tagastus["X"] += 1
    return(tagastus)


print(võitja([
            ['O',' ',' ','X'],
            [' ','O','X',' '],
            [' ','X','O',' '],
            ['X',' ',' ','O']]))