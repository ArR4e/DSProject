#2. Trips-traps-trull
def kas_on_korduvaid(rida):
    eelmine=0
    elemente=1
    riste=0
    ringe=0
    for element in rida:
        if element==" ":
            eelmine=element
            continue
        praegune=element
        if eelmine==praegune:
            elemente+=1
            if elemente==3:
                if praegune=="X":
                    riste+=1
                if praegune=="O":
                    ringe+=1
                elemente-=1
        else:
            elemente=1
        eelmine=element
    return riste, ringe
    

def võitja(maatriks):
    sõnaraamat={'X': 0, 'O': 0}
#     #ridadel korduvad
    for rida in maatriks:
        tulemus=kas_on_korduvaid(rida)
        sõnaraamat['X']+=tulemus[0]
        sõnaraamat['O']+=tulemus[1]
    #veergudel korduvad
    i=0
    while i < 4:
        veerg=[]
        for rida in maatriks:
            veerg.append(rida[i]) 
        tulemus=kas_on_korduvaid(veerg)
        sõnaraamat['X']+=tulemus[0]
        sõnaraamat['O']+=tulemus[1]
        i+=1
    #peadiagonaali korduvad
    j=-1
    while j<2:
        i=0
        diagonaal=[]
        for rida in maatriks:
            indeks=i+j
            if indeks>3 or indeks<0:
                diagonaal.append(' ')
            else:
                diagonaal.append(rida[indeks])
            i+=1
        tulemus=kas_on_korduvaid(diagonaal)
        sõnaraamat['X']+=tulemus[0]
        sõnaraamat['O']+=tulemus[1]
        j+=1
    #kõrvaldiagonaali korduvad
    j=1
    while abs(j)<3:
        i=-1
        diagonaal=[]
        for rida in maatriks:
            indeks=i+j
            if abs(indeks)>4 or indeks>=0:
                diagonaal.append(' ')
            else:
                diagonaal.append(rida[indeks])
            i-=1
        tulemus=kas_on_korduvaid(diagonaal)
        sõnaraamat['X']+=tulemus[0]
        sõnaraamat['O']+=tulemus[1]
        j-=1
    return sõnaraamat
                
        
# print(võitja([['O','O','O','O'],
#             ['X','O','X',' '],
#             [' ','X','O',' '],
#             ['X',' ',' ','O']]))