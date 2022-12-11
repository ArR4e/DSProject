# 3. Sünnikuupäev isikukoodist

def sünnikuupäev(isikukood):
    
    päev = isikukood[5:7]
    
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    
    mitmes_kuu = int(isikukood[3:5])

    kuu = kuud[mitmes_kuu -1]
    
    if int(isikukood[0]) == 1 or int(isikukood[0]) == 2:
        aasta = "18" + isikukood[1:3]
    if int(isikukood[0]) == 3 or int(isikukood[0]) ==4:
        aasta = "19" + isikukood[1:3]
    if int(isikukood[0]) == 5 or int(isikukood[0]) ==6:
        aasta = "20" + isikukood[1:3]
    
    sünnikuupäev = päev + ". " + kuu + " " + aasta
    return sünnikuupäev
print(sünnikuupäev("34501234215"))