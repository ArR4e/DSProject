def võitja(mängulaud):
    kordused = {'O':0, 'X':0}
    
    tulemused= {}
    
    tulemused['ho'] = leia_horisontaalne(mängulaud, "O")
    tulemused['hx'] = leia_horisontaalne(mängulaud, "X")
    
    tulemused['vo'] = leia_vertikaalne(mängulaud, "O")
    tulemused['vx'] = leia_vertikaalne(mängulaud, "X")
    
    tulemused['dpo'] = leia_peadiagonaalne(mängulaud, "O")
    tulemused['dpx'] = leia_peadiagonaalne(mängulaud, "X")
    
    tulemused['dko'] = leia_kõrvaldiagonaalne(mängulaud, "O")
    tulemused['dkx'] = leia_kõrvaldiagonaalne(mängulaud, "X")
    
    for tulemus in tulemused:
        if "O" in tulemused[tulemus]:
            kordused['O'] = kordused['O'] + tulemused[tulemus]['O']
        else:
            kordused['X'] = kordused['X'] + tulemused[tulemus]['X']
            
    return kordused

def leia_horisontaalne(mängulaud, sümbol):
    kolmeseid_kordusi = 0
    for i in range(4):
        for j in range(2):
            if mängulaud[i][j] == mängulaud[i][j+1] == mängulaud[i][j+2] == sümbol:
                kolmeseid_kordusi += 1
                
    return {sümbol:kolmeseid_kordusi}

def leia_vertikaalne(mängulaud, sümbol):
    kolmeseid_kordusi = 0
    for i in range(2):
        for j in range(4):
            if mängulaud[i][j] == mängulaud[i+1][j] == mängulaud [i+2][j] == sümbol:
                kolmeseid_kordusi += 1
                
    return {sümbol:kolmeseid_kordusi}
            
def leia_peadiagonaalne(mängulaud, sümbol):
    kolmeseid_kordusi = 0
    for i in range(2):
        for j in range(2):
            if mängulaud[j][i] == mängulaud[j+1][i+1] == mängulaud[j+2][i+2] == sümbol:
                kolmeseid_kordusi += 1
    return {sümbol:kolmeseid_kordusi}
            
            
def leia_kõrvaldiagonaalne(mängulaud, sümbol):
    kolmeseid_kordusi = 0
    for i in range(2):
        for j in range(2):
            if mängulaud[i][j+1] == mängulaud[i+1][j] == sümbol:
                kolmeseid_kordusi += 1
                
    return {sümbol:kolmeseid_kordusi}
            
            
    
        
        
        
        
        