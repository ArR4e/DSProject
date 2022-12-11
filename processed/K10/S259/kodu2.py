def võitudearv(m, sümbol): #abif, mis loeb kokku, mitu korda etteantud sümbol võitnud
    
    kokku = 0
    
    #reas 3 sümbolit
    #pos [i][j] näitab võimaliku rea algust
    for i in range(len(m)):
        for j in range(len(m[i])-2):
            if m[i][j] == m[i][j+1] == m[i][j+2] == sümbol:
                kokku += 1
    
    #veerus 3 sümbolit järjest
    for i in range(len(m)-2):
        for j in range(len(m[i])):
            if m[i][j] == m[i+1][j] == m[i+2][j] == sümbol:
                kokku += 1
    
    #mööda üht diagonaali
    for i in range(len(m)-2):
        for j in range(len(m[i])-2):
            if m[i][j] == m[i+1][j+1] == m[i+2][j+2] == sümbol:
                kokku += 1
    
    #mööda teist diagonaali
    for i in range(len(m)-2):
        for j in range(len(m[i])-2):
            if m[i][j] == m[i+1][j-1] == m[i+2][j-2] == sümbol:
                kokku += 1
    return kokku

#põhif kasutame abif kummagi sümboli puhul
def võitja(m):
    võite_O = võitudearv(m,'O')
    võite_X = võitudearv(m, 'X')
    return {'O': võite_O, 'X': võite_X}
