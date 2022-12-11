# 2. Trips-traps-trull
# Kirjuta funktsioon võitja, mis võtab argumendiks maatriksina (st listide listina) esitatud 4×4-ruudustikuga trips-traps-trulli mängu seisu.
# Funktsioon tagastab sõnastiku, kus võtmeteks on sümbolid 'O' (so suurtäht O, mitte null) ja 'X'. Kummagi võtme väärtuseks on arv, mis näitab,
# mitu korda esineb see sümbol ruudustikus kolm korda järjest horisontaalselt, vertikaalselt või diagonaalselt.

# NB! Mängu seis ei pruugi olla alati korrektne (st 'O' ja 'X' esinemiste arv ruudustikul võib erineda rohkem kui ühe võrra).

# Näide 1.
# >>> võitja([[' ',' ',' ',' '],
#            [' ',' ',' ',' '],
#            [' ',' ',' ',' '],
#            [' ',' ',' ',' ']])
# {'O': 0, 'X': 0}

# Näide 2.
# >>> võitja([['X','X','X',' '],
#            [' ','O',' ',' '],
#            [' ',' ','O',' '],
#            [' ',' ',' ','O']])
# {'O': 1, 'X': 1}

# Näide 3.
# >>> võitja([['O',' ',' ','X'],
#            [' ','O','X',' '],
#            [' ','X','O',' '],
#            ['X',' ',' ','O']])
# {'O': 2, 'X': 2}
# (Neljase rea koosseisus on kaks kolmest rida – esimesed kolm elementi ja viimased kolm elementi.)

# Näide 4.
# >>> võitja([['O',' ','O','X'],
#            ['O','O','X','X'],
#            ['O','X','O',' '],
#            ['X','X','X','O']])
# {'O': 4, 'X': 3}

def võitja(m):
    
    # Read
    O_read = 0
    X_read = 0
    for i in range(4):
        for j in range(2):
            if m[i][j] == m[i][j+1] == m[i][j+2] == "O":
                O_read += 1
            elif m[i][j] == m[i][j+1] == m[i][j+2] == "X":
                X_read += 1
    
    # Veerud
    O_veerud = 0
    X_veerud = 0
    for i in range(2):
        for j in range(4):
            if m[i][j] == m[i+1][j] == m[i+2][j] == "O":
                O_veerud += 1
            elif m[i][j] == m[i+1][j] == m[i+2][j] == "X":
                X_veerud += 1
                
    # Diagonaalid vasakult paremale
    O_pd1 = 0
    X_pd1 = 0
    for i in range(2):
        for j in range(2):
            if m[i][j] == m[i+1][j+1] == m[i+2][j+2] == "O":
                O_pd1 += 1
            elif m[i][j] == m[i+1][j+1] == m[i+2][j+2] == "X":
                X_pd1 += 1
    
    # Diagonaalid paremalt vasakule
    O_pd2 = 0
    X_pd2 = 0
    for i in range(2):
        for j in range(2,0,-1):
            if m[i][j+1] == m[i+1][j] == m[i+2][j-1] == "O":
                O_pd2 += 1
            elif m[i][j+1] == m[i+1][j] == m[i+2][j-1] == "X":
                X_pd2 += 1
                
    
    O_kokku = O_read + O_veerud + O_pd1 + O_pd2
    X_kokku = X_read + X_veerud + X_pd1 + X_pd2
    
    d = {'O' : O_kokku, 'X' : X_kokku}

    return d

# Kommentaar: murelahendaja näpunäiteid olid väga kasulikud, et jõuda lahendusele lähemale!
    