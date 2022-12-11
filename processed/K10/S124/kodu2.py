#murelahendaja_aitas_välja
def võitja(maatriks):
    kombinatsioonid = []
    sõ = {}
    x = 0
    o = 0
#   see pole tegelikult minu koodis liiga vajalik, oleks saanud selle efektiivsemalt tööle panna kindlasti.
    for rida in maatriks:
        for el in rida:
            if el == 'X':
                x += 1
            if el == 'O':
                o += 1
                
    if x > 2 or o > 2:
                
        for i in range(4):
            for j in range(2):
                kombinatsioonid += [maatriks[i][j]+maatriks[i][j+1]+maatriks[i][j+2]]
                
        for i in range(2):
            for j in range(4):
                kombinatsioonid += [maatriks[i][j]+maatriks[i+1][j]+maatriks[i+2][j]]
        
        for i in range(2):
            for j in range(2):
                kombinatsioonid += [maatriks[i][j]+maatriks[i+1][j+1]+maatriks[i+2][j+2]]
        
        for i in range(2):
            for j in range(2):
                kombinatsioonid += [maatriks[i][j+2]+maatriks[i+1][j+1]+maatriks[i+2][j]]
    

    sõ['X'] = sõ.get('X', kombinatsioonid.count('XXX'))
    sõ['O'] = sõ.get('O', kombinatsioonid.count('OOO'))
    
    return sõ
    
# print(võitja([['O',' ',' ','X'],
#             [' ','O','X',' '],
#             [' ','X','O',' '],
#             ['X',' ',' ','O']]))

    