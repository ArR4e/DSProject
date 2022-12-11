def sünnikuupäev(isikukood):
    aasta = isikukood[1:3]
    if isikukood[0] == "1" or isikukood[0] == "2":
        sünniaasta = ("18" + str(aasta))
    if isikukood[0] == "3" or isikukood[0] == "4":
        sünniaasta = ("19" + str(aasta))
    if isikukood[0] == "5" or isikukood[0] == "6":
        sünniaasta = ("20" + str(aasta))
    kuu = isikukood[3:5]
    if kuu == "01":
        sünnikuu = "jaanuar"
    if kuu == "02":
        sünnikuu = "veebruar"
    if kuu == "03":
        sünnikuu = "märts"
    if kuu == "04":
        sünnikuu = "aprill"
    if kuu == "05":
        sünnikuu = "mai"
    if kuu == "06":
        sünnikuu = "juuni"
    if kuu == "07":
        sünnikuu = "juuli"
    if kuu == "08":
        sünnikuu = "august"
    if kuu == "09":
        sünnikuu = "september"
    if kuu == "10":
        sünnikuu = "oktoober"
    if kuu == "11":
        sünnikuu = "november"
    if kuu == "12":
        sünnikuu = "detsember"
    kuupäev = isikukood[5:7]
    
    return (kuupäev + ". " + str(sünnikuu) + " " + str(sünniaasta))

