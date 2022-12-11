def võitja(maatriks):
    summa = [0,0]
    for i in range(len(maatriks)): #rea kaupa
        x = y =tühi = 0
        for j in range(len(maatriks[i])):
            if maatriks[i][j] == 'X':
                if y!=0:
                    if j ==1:
                        y=0
                    else:
                        break
                x+=1
            elif maatriks[i][j] == 'O':
                if x!=0:
                    if j ==1:
                        x=0
                    else:
                        break
                y+=1
            elif maatriks[i][j] == '0':
                tühi = j
        if x == 4:
            summa[0]+=2
        elif y == 4:
            summa[1]+=2
        else:
            if tühi!= 2 and tühi!= 3:
                if x == 3:
                    summa[0]+=1
                if y == 3:
                    summa[1]+=1
    for i in range(len(maatriks)): #veeru kaupa
        x = y = tühi = 0
        for j in range(len(maatriks[i])):
            if maatriks[j][i] == 'X':
                if y!=0:
                    if j ==1:
                        y=0
                    else:
                        break
                x+=1
            elif maatriks[j][i] == 'O':
                if x!=0:
                    if j ==1:
                        x=0
                    else:
                        break
                y+=1
            else:
                tühi = j
        if x == 4:
            summa[0]+=2
        elif y == 4:
            summa[1]+=2
        else:
            if tühi!= 1 and tühi!= 2:
                if x == 3:
                    summa[0]+=1
                if y == 3:
                    summa[1]+=1
    kaks = [0,3]
    if maatriks[0][0] == maatriks [1][1] == maatriks[2][2] == 'X':
        summa[0]+=1
    if maatriks[0][0] == maatriks [1][1] == maatriks[2][2] == 'O':
        summa[1]+=1
    if maatriks[0][1] == maatriks [1][2] == maatriks[2][3] == 'X':
        summa[0]+=1
    if maatriks[0][1] == maatriks [1][2] == maatriks[2][3] == 'O':
        summa[1]+=1
    if maatriks[1][0] == maatriks [2][1] == maatriks[3][2] == 'X':
        summa[0]+=1
    if maatriks[1][0] == maatriks [2][1] == maatriks[3][2] == 'O':
        summa[1]+=1
    if maatriks[1][1] == maatriks [2][2] == maatriks[3][3] == 'X':
        summa[0]+=1
    if maatriks[1][1] == maatriks [2][2] == maatriks[3][3] == 'O':
        summa[1]+=1
    if maatriks[2][0] == maatriks [1][1] == maatriks[0][2] == 'X':
        summa[0]+=1
    if maatriks[2][0] == maatriks [1][1] == maatriks[0][2] == 'O':
        summa[1]+=1
    if maatriks[2][1] == maatriks [1][2] == maatriks[0][3] == 'X':
        summa[0]+=1
    if maatriks[2][1] == maatriks [1][2] == maatriks[0][3] == 'O':
        summa[1]+=1
    if maatriks[3][0] == maatriks [2][1] == maatriks[1][2] == 'X':
        summa[0]+=1
    if maatriks[3][0] == maatriks [2][1] == maatriks[1][2] == 'O':
        summa[1]+=1
    if maatriks[3][1] == maatriks [2][2] == maatriks[1][3] == 'X':
        summa[0]+=1
    if maatriks[3][1] == maatriks [2][2] == maatriks[1][3] == 'O':
        summa[1]+=1
    return {'O':summa[1],'X':summa[0]}