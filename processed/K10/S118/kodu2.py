from numpy import *

def ridade_kontroll(ruudustik, seis):
    for rida in ruudustik:
        for element in [rida[0], rida[3]]:
            if element == "X" or element == "O":
                if rida[1] == element and rida[2] == element:
                    seis[element]+=1
    return seis

def kolmik_kontroll(kolmik, seis):
    if kolmik[0] == "X" or kolmik[0] == "O":
        if kolmik[0] == kolmik[1] and kolmik[1] == kolmik[2]:
            seis[kolmik[0]]+=1
    return seis

def võitja(ruudustik):
    #ridade_kontroll
    seis = {"O": 0,"X": 0}
    seis = ridade_kontroll(ruudustik, seis)
    transponeeritud = [[],[],[],[]]
    for rida in ruudustik:
        for indeks in range(0,4):
            transponeeritud[indeks].append(rida[indeks])
    seis = ridade_kontroll(transponeeritud, seis)
    diagonaalid = [[],[]]
    for indeks in range(0,4):
        diagonaalid[0].append(ruudustik[indeks][indeks])
        diagonaalid[1].append(ruudustik[indeks][3-indeks])
    seis = ridade_kontroll(diagonaalid, seis)
    ruudustik_np = array(ruudustik)
    for i in [1,-1]:
        seis = kolmik_kontroll(ruudustik_np.diagonal(i), seis)
    for i in [1,-1]:
        seis = kolmik_kontroll(fliplr(ruudustik_np).diagonal(i), seis)
    return seis
                

        
"""print(võitja([['O',' ','O','X'],
            ['O','O','X','X'],
            ['O','X','O',' '],
            ['X','X','X','O']]))"""
