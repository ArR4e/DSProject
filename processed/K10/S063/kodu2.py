'''-- Kodutöö nr. 10 - 2. Trips-traps-trull --'''
'''Funktsioon 'võitja' võtab argumendiks maatriksina esitatud 4×4-ruudustikuga trips-traps-trulli mängu seisu.
   Funktsioon tagastab sõnastiku, kus võtmeteks on suured tähed 'O' ja 'X' ning väärtuseks on arv, mis näitab,
   mitu korda esineb see sümbol ruudustikus kolm korda järjest horisontaalselt, vertikaalselt või diagonaalselt.'''
########################################################################################################################################
def võitja(ruudustik):
    # tagastatav sõnastik
    sõnastik = {}
    
    # tagastatavad 'XXX' ja 'OOO' esinemiste arvud
    o_arv = 0
    x_arv = 0
    
    # esinemised horisontaalselt järjest kas 'X'id või 'O'd
    for i in range(0, 4):
        for j in range(0, 2):
            if ruudustik[i][j] == 'X' and ruudustik[i][j+1] == 'X' and ruudustik[i][j+2] == 'X':
                x_arv += 1
            if ruudustik[i][j] == 'O' and ruudustik[i][j+1] == 'O' and ruudustik[i][j+2] == 'O':
                o_arv += 1
    # esinemised vertikaalselt järjest kas 'X'id või 'O'd
    for i in range(0, 2):
        for j in range(0, 4):
            if ruudustik[i][j] == 'X' and ruudustik[i+1][j] == 'X' and ruudustik[i+2][j] == 'X':
                x_arv += 1
            if ruudustik[i][j] == 'O' and ruudustik[i+1][j] == 'O' and ruudustik[i+2][j] == 'O':
                o_arv += 1
    # esinamised diagonaalselt vasakult paremale järjest kas 'X'id või 'O'd 
    for i in range(0, 2):
        for j in range(0, 2):
            if ruudustik[i][j] == 'X' and ruudustik[i+1][j+1] == 'X' and ruudustik[i+2][j+2] == 'X':
                x_arv += 1
            if ruudustik[i][j] == 'O' and ruudustik[i+1][j+1] == 'O' and ruudustik[i+2][j+2] == 'O':
                o_arv += 1
    # esinemised diagonaalselt paremalt vasakule kas 'X'id või 'O'd        
    for i in range(0, 2):
        for j in range(2, 4):
            if ruudustik[i][j] == 'X' and ruudustik[i+1][j-1] == 'X' and ruudustik[i+2][j-2] == 'X':
                x_arv += 1
            if ruudustik[i][j] == 'O' and ruudustik[i+1][j-1] == 'O' and ruudustik[i+2][j-2] == 'O':
                o_arv += 1
    
    sõnastik['O'] = o_arv
    sõnastik['X'] = x_arv
    
    return sõnastik
########################################################################################################################################
print(võitja([['O',' ','O','X'],
              ['O','O','X','X'],
              ['O','X','O',' '],
              ['X','X','X','O']]))
print(võitja([[' ',' ',' ',' '],
              [' ',' ',' ',' '],
              [' ',' ',' ',' '],
              [' ',' ',' ',' ']]))