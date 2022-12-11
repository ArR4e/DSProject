def sünnikuupäev(isikukood):
    päev = 0
    kuu = 0
    aasta = 0
    if int(isikukood[0]) < 3:
        aasta = str(18)
        aasta += str(isikukood[1:3])
        kuu = str(isikukood[3:5])
        päev = int(isikukood[5:7])
    elif int(isikukood[0]) == 3:
        aasta = str(19)
        aasta += str(isikukood[1:3])
        kuu = str(isikukood[3:5])
        päev = int(isikukood[5:7])
    elif int(isikukood[0]) == 4:
        aasta = str(19)
        aasta += str(isikukood[1:3])
        kuu = str(isikukood[3:5])
        päev = int(isikukood[5:7])
    elif int(isikukood[0]) == 5:
        aasta = str(20)
        aasta += str(isikukood[1:3])
        kuu = str(isikukood[3:5])
        päev = int(isikukood[5:7])
    elif int(isikukood[0]) == 6:
        aasta = str(20)
        aasta += str(isikukood[1:3])
        kuu = str(isikukood[3:5])
        päev = int(isikukood[5:7])
    
    kuunimi = 0
    
    if kuu == "01":
        kuunimi = "jaanuar"
    if kuu == "02":
        kuunimi = "veebruar"
    if kuu == "03":
        kuunimi = "märts"
    if kuu == "04":
        kuunimi = "aprill"
    if kuu == "05":
        kuunimi = "mai"
    if kuu == "06":
        kuunimi = "juuni"
    if kuu == "07":
        kuunimi = "juuli"
    if kuu == "08":
        kuunimi = "august"
    if kuu == "09":
        kuunimi = "september"
    if kuu == "10":
        kuunimi = "oktoober"
    if kuu == "11":
        kuunimi = "november"
    if kuu == "12":
        kuunimi = "detsember"
    
    sünnikuupäev = str(päev) + ". " + str(kuunimi) + " " + str(aasta)
     
    return(sünnikuupäev)
    

