from copy import deepcopy
def võitja(maatriks):
    tulemused = {"O": 0, "X": 0}
    for kogu in maatriks:
        for rida in range(len(kogu)):
            if rida >= 2:
                break
            elif kogu[rida] == kogu[rida + 1] == kogu[rida + 2]:
                if kogu[rida] != "O" and kogu[rida] != "X":
                    continue
                tulemused[kogu[rida]] += 1
            elif kogu[rida] == kogu[rida + 1] == kogu[rida + 2] == kogu[rida + 4]:
                if kogu[rida] != "O" and kogu[rida] != "X":
                    continue
                tulemused[kogu[rida]] += 2

    pööratud_maatriks = deepcopy(maatriks)
    for i in range(len(maatriks)):
        for j in range(len(maatriks[0])):
            pööratud_maatriks[j][i] = maatriks[i][j]
    for kogu1 in pööratud_maatriks:
        for rida1 in range(len(kogu1)):
            if rida1 >= 2:
                break
            elif kogu1[rida1] == kogu1[rida1 + 1] == kogu1[rida1 + 2]:
                if kogu1[rida1] != "O" and kogu1[rida1] != "X":
                    continue
                tulemused[kogu1[rida1]] += 1
            elif kogu1[rida1] == kogu1[rida1 + 1] == kogu1[rida1 + 2] == kogu1[rida1 + 4]:
                if kogu1[rida1] != "O" and kogu1[rida1] != "X":
                    continue
                tulemused[kogu1[rida1]] += 2
                
    for kogu2 in range(len(maatriks)-1):
        if kogu2 >= 2:
            break
        for rida2 in range(len(maatriks)-1):
            if rida2 >= 2:
                break
            elif maatriks[kogu2][rida2] == maatriks[kogu2 + 1][rida2 + 1] == maatriks[kogu2 + 2][rida2 + 2]:
                if maatriks[kogu2][rida2] != "O" and maatriks[kogu2][rida2] != "X":
                    continue
                tulemused[maatriks[kogu2][rida2]] += 1
            elif maatriks[kogu2][rida2] == maatriks[kogu2 + 1][rida2 + 1] == maatriks[kogu2 + 2][rida2 + 2] == maatriks[kogu2 + 3][rida2 + 3]:
                if maatriks[kogu2][rida2] != "O" and maatriks[kogu2][rida2] != "X":
                    continue
                tulemused[maatriks[kogu2][rida2]] += 2
                
    pööratud = []            
    pööratud += [maatriks[0][::-1]] + [maatriks[1][::-1]] + [maatriks[2][::-1]] + [maatriks[3][::-1]]
    for kogu2 in range(len(pööratud)-1):
        if kogu2 >= 2:
            break
        for rida2 in range(len(pööratud)-1):
            if rida2 >= 2:
                break
            elif pööratud[kogu2][rida2] == pööratud[kogu2 + 1][rida2 + 1] == pööratud[kogu2 + 2][rida2 + 2]:
                if pööratud[kogu2][rida2] != "O" and pööratud[kogu2][rida2] != "X":
                    continue
                tulemused[pööratud[kogu2][rida2]] += 1
            elif pööratud[kogu2][rida2] == pööratud[kogu2 + 1][rida2 + 1] == pööratud[kogu2 + 2][rida2 + 2] == pööratud[kogu2 + 3][rida2 + 3]:
                if pööratud[kogu2][rida2] != "O" and pööratud[kogu2][rida2] != "X":
                    continue
                tulemused[pööratud[kogu2][rida2]] += 2
                
    return tulemused