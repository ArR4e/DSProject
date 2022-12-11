def sünnikuupäev(kood):
    kood = str(kood)
    sajand = int(kood[0])
    
    if sajand == 1 or sajand == 2:
        algus = "18"
        
    if sajand == 3 or sajand == 4:
        algus = "19"
        
    if sajand == 5 or sajand == 6:
        algus = "20"
        
    if sajand == 7 or sajand == 8:
        algus = "21"
    
    aasta = kood[1]+kood[2]
    
    aasta = algus+aasta
    
    kuu = int(kood[3]+kood[4])
    
    kuud = ["jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
    
    kuu = kuud[kuu-1]
    
    päev = kood[5]+kood[6]
    
    kuupäev = päev + ". " + kuu + " " + aasta
    
    return kuupäev
    