def sünnikuupäev(isikukood):
    järjend = []
    for i in isikukood:
        järjend.append(i)
    päev = str(järjend[5]) + str(järjend[6]) + "."
    kuu = str(järjend[3]) + str(järjend[4])
    aasta1 = int(järjend[0])
    aasta2 = str(järjend[1]) + str(järjend[2])
    if aasta1 == 1 or aasta1 == 2:
        aasta1 = "18"
    elif aasta1 == 3 or aasta1 == 4:
        aasta1 = "19"
    elif aasta1 == 5 or aasta1 == 6:
        aasta1 = "20"
    aasta = aasta1 + aasta2
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

print(sünnikuupäev("50106242714"))
    
    