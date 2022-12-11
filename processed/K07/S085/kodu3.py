def sünnikuupäev(isikukood):
    päev = isikukood[5:7]
    kuu_nr = int(isikukood[3:5])
    
    kuude_järjend = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    kuu = kuude_järjend[kuu_nr - 1]
    a = int(isikukood[0:1])
    if a == 1 or a == 2:
        b = 18
    elif a == 3 or a == 4:
        b = 19
    else:
        b = 20
        
    aasta = str(b) + isikukood[1:3]
    sünnikuupäev = päev + ". "+ kuu + " " + aasta
    return sünnikuupäev

