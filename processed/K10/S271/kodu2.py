def võitja(maatriks):
    tulemus = {'O':0, 'X':0}
    for i in range(4):
        if maatriks[i] == ['X','X','X',' '] or maatriks[i] == ['O','X','X','X'] or maatriks[i] == ['X','X','X','O'] or maatriks[i] == ['O','X','X','X']:
            tulemus['X'] = tulemus['X']+1
        elif maatriks[i] == ['O','O','O',' '] or maatriks[i] == [' ','O','O','O'] or maatriks[i] == ['X','O','O','O'] or maatriks[i] == ['O','O','O','X']:
            tulemus['O'] = tulemus['O']+1
        elif maatriks[i] == ['X','X','X','X']:
            tulemus['X'] = tulemus['X']+2
            print(1)
        elif maatriks[i] == ['O','O','O','O']:
            tulemus['O'] = tulemus['O']+2
            print(2)
        for j in range(4):
            if j < 2 and i < 2:
                if maatriks[i][j] == maatriks[i+1][j+1] and maatriks[i][j] == maatriks[i+2][j+2]:
                    if maatriks[i][j] == 'O':
                        tulemus['O'] = tulemus['O']+1
                    elif maatriks[i][j] == 'X':
                        tulemus['X'] = tulemus['X']+1
            if i < 2 and j > 1:
                if maatriks[i][j] == maatriks[i+1][j-1] and maatriks[i][j] == maatriks[i+2][j-2]:
                    if maatriks[i][j] == 'O':
                        tulemus['O'] = tulemus['O']+1
                    elif maatriks[i][j] == 'X':
                        tulemus['X'] = tulemus['X']+1
            if i < 2:
                if maatriks[i][j] == maatriks[i+1][j] and maatriks[i][j] == maatriks[i+2][j]:
                    if maatriks[i][j] == 'O':
                        tulemus['O'] = tulemus['O']+1
                    elif maatriks[i][j] == 'X':
                        tulemus['X'] = tulemus['X']+1
    return tulemus
                    