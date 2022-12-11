def võitja(maatriks):
    tulem = {'O': 0, 'X': 0}
    
    tulem['O'] += kas_rida_ja_tulp(maatriks,'O')
    tulem['X'] += kas_rida_ja_tulp(maatriks,'X')
    
    tulem['O'] += kas_diagonaal(maatriks, 'O')
    tulem['X'] += kas_diagonaal(maatriks, 'X')
    
    return tulem
    
    
    
def kas_rida_ja_tulp(maatriks, täht):
    counter = 0
    tulp1 = ''
    tulp2 = ''
    tulp3 = ''
    tulp4 = ''
    
    for i in maatriks:
        
        #moodustan tulbad
        tulp1 += i[0]
        tulp2 += i[1]
        tulp3 += i[2]
        tulp4 += i[3]
        
        #tegelen ridadega
        sõne = ''.join(i)
        
        if täht*4 in sõne:
            counter += 2
        elif täht*3 in sõne:
            counter += 1
        
    tulbad = tulp1 +' '+ tulp2 +' '+ tulp3 +' '+ tulp4
    tulbad = tulbad.split(" ")
    
    #vaatan, kas tulpades piisavalt järjest
    for i in range(len(tulbad)):
        if täht*4 in tulbad[i]:
            counter += 2
        elif täht*3 in tulbad[i]:
            counter += 1
        
    return counter

def kas_diagonaal(maatriks, täht):
    counter = 0
    mis_rida = 0
    
    #ma siiralt väga vabandan, koolis liiga kiire, et mõelda
    diagonaal1 = ''
    diagonaal2 = ''
    diagonaal3 = ''
    diagonaal4 = ''
    diagonaal5 = ''
    diagonaal6 = ''
    
    for i in range(len(maatriks)):
        
        diagonaal1 += maatriks[i][i]
        
        if i < 3:
            diagonaal2 += maatriks[i][i+1]
            
            diagonaal5 += maatriks[i+1][i]
            
            diagonaal3 += maatriks[i][-(i+2)]
            
            diagonaal6 += maatriks[i+1][-(i+1)]
        
        diagonaal4 += maatriks[i][-(i+1)]
        
    diagonaalid = diagonaal1+' '+diagonaal2+' '+diagonaal3+' '+diagonaal4+' '+diagonaal5+' '+diagonaal6
        
    diagonaalid = diagonaalid.split(' ')
        
    for i in diagonaalid:
        if täht*4 in i:
            counter += 2
        elif täht*3 in i:
            counter += 1
    return counter
        
        
        
            
            # d1 d2  d3  d4
maatriks = [['X','X',' ','X'],
            ['X',' ','X',' '],#d6
            ['X','X',' ','X'],
            ['X',' ','X',' ']]

print(võitja(maatriks))
