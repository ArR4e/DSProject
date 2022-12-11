# 3. Sünnikuupäev isikukoodist / RP

def sünnikuupäev(isikukood):
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    
    päev = isikukood[5:7]
    kuu_nr = isikukood[3:5]
    aasta = isikukood[1:3]
    
    #Õige aasta leidmine
    if int(isikukood[0]) in [3,4]:
        aasta = "19" + aasta
    elif int(isikukood[0]) in [1,2]:
        aasta = "18" + aasta
    else:
        aasta = "20" + aasta
        
    #Õige kuu leidmine
    kuu = kuud[int(kuu_nr)-1]
    
    return päev + ". " + kuu + " " + aasta

print(sünnikuupäev('50110012787'))