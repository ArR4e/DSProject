def sünnikuupäev (isikukood):
    isikukood = list(isikukood)
    kuup1 = isikukood[5]
    kuup2 = isikukood[6]
    if isikukood[0] == "5" or isikukood[0]== "6":
        aasta1 = "20"
    elif isikukood[0] == "7" or isikukood[0]== "8":
        aasta1 = "21"
    elif isikukood[0] == "3" or isikukood[0]== "4":
        aasta1 = "19"
    else:
        aasta1 = "18"
    aasta2 = isikukood[1]
    aasta3 =isikukood[2]
    kuu1 = isikukood[3]
    kuu2 =isikukood[4]
    kuu = kuu1 + kuu2
    if kuu == "01":
        kuu = "jaanuar"
    elif kuu == "02":
        kuu = "veebruar"
    elif kuu == "03":
        kuu = "märts"
    elif kuu == "04":
        kuu = "aprill"
    elif kuu == "05":
        kuu = "mai"
    elif kuu == "06":
        kuu = "juuni"
    elif kuu == "07":
        kuu = "juuli"
    elif kuu == "08":
        kuu = "august"
    elif kuu == "09":
        kuu = "september"
    elif kuu == "10":
        kuu = "oktoober"
    elif kuu == "11":
        kuu = "november"
    else:
        kuu = "detsember"
    global sünnikuupäev
    sünnikuupäev = kuup1 + kuup2 + ". " + kuu + " " + aasta1 + aasta2 + aasta3
    return sünnikuupäev

isikukood = str(input("Sisesta oma isikukood"))
sünnikuupäev (isikukood)
print("Isiku sünnikuupäev on: " + sünnikuupäev)