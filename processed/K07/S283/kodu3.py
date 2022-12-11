def sünnikuupäev(isikukood):
    järjend = []
    for i in isikukood:
        järjend.append(i)
    päev = str(järjend[5]) + str(järjend[6]) + "."
    kuu = str(järjend[3]) + str(järjend[4])
    aasta_esimesed = int(järjend[0])
    aasta_viimased = str(järjend[1]) + str(järjend[2])
    if aasta_esimesed == 1 or aasta_esimesed == 2:
        aasta_esimesed = "18"
    elif aasta_esimesed == 3 or aasta_esimesed == 4:
        aasta_esimesed = "19"
    elif aasta_esimesed == 5 or aasta_esimesed == 6:
        aasta_esimesed = "20"
    aasta = aasta_esimesed + aasta_viimased
    if kuu == "01":
        kuu = " jaanuar "
    elif kuu == "02":
        kuu = " veebruar "
    elif kuu == "03":
        kuu = " märts "
    elif kuu == "04":
        kuu = " aprill "
    elif kuu == "05":
        kuu = " mai "
    elif kuu == "06":
        kuu = " juuni "
    elif kuu == "07":
        kuu = " juuli "
    elif kuu == "08":
        kuu = " august "
    elif kuu == "09":
        kuu = " september "
    elif kuu == "10":
        kuu = " oktoober "
    elif kuu == "11":
        kuu = " november "
    elif kuu == "12":
        kuu = " detsember "        
    return (päev + kuu + aasta)

print(sünnikuupäev("29802158384"))