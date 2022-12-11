def võitja(maatriks):
    O = 0
    X = 0
    transformeeritud = [[0, 0, 0, 0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(4):
        for j in range(4):
            transformeeritud[j][i] = maatriks[i][j]
    pohidiagonaalid = [[0,0,0,0],[0,0,0,0]]
    korvaldiagonaalid = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    for i in range(4):
        pohidiagonaalid[0][i] = maatriks[i][i] 
        pohidiagonaalid[1][i] = maatriks[i][3-i]
    for i in range(3):
        korvaldiagonaalid[0][i] = maatriks[i][i+1]
        korvaldiagonaalid[1][i] = maatriks[i+1][i]
        korvaldiagonaalid[2][i] = maatriks[i][2-i]
        korvaldiagonaalid[3][i] = maatriks[i+1][3-i]
    for rida in maatriks:
        if rida.count('X')==4:
            X+=2
        elif rida.count('O')==4:
            O+=2
        elif rida.count('X')==3 and ((rida.index(' ') if ' ' in rida else None) in [0,3] or (rida.index('O')  if 'O' in rida else None) in [0,3]):
            X+=1
        elif rida.count('O')==3 and ((rida.index(' ') if ' ' in rida else None) in [0,3] or (rida.index('X')  if 'X' in rida else None) in [0,3]):
            O+=1
            
    for rida in transformeeritud:
        if rida.count('X')==4:
            X+=2
        elif rida.count('O')==4:
            O+=2
        elif rida.count('X')==3 and ((rida.index(' ') if ' ' in rida else None) in [0,3] or (rida.index('O')  if 'O' in rida else None) in [0,3]):
            X+=1
        elif rida.count('O')==3 and ((rida.index(' ') if ' ' in rida else None) in [0,3] or (rida.index('X')  if 'X' in rida else None) in [0,3]):
            O+=1
    for diagonaal in korvaldiagonaalid:
        if diagonaal.count('O')==3:
            O+=1
        elif diagonaal.count('X')==3:
            X+=1
    for diagonaal in pohidiagonaalid:
        if diagonaal.count('X')==4:
            X+=2
        elif diagonaal.count('O')==4:
            O+=2
        elif diagonaal.count('X')==3 and ((diagonaal.index(' ') if ' ' in diagonaal else None) in [0,3] or (diagonaal.index('O') if 'O' in diagonaal else None) in [0,3]):
            X+=1
        elif diagonaal.count('O')==3 and ((diagonaal.index(' ') if ' ' in diagonaal else None) in [0,3] or (diagonaal.index('X') if 'X' in diagonaal else None) in [0,3]):
            O+=1
    return {'O':O,'X':X}
print(võitja([['O',' ','O','X'],
            ['O','O','X','X'],
            ['O','X','O',' '],
            ['X','X','X','O']]))