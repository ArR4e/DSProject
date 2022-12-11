def sünnikuupäev(isikukood):
    päev = ""
    kuu = ""
    aasta = ""
    for n in isikukood:
        if len(aasta) < 2:
            if 1 <= int(n) <= 2:
                aasta += "18"
            elif 3 <= int(n) <= 4:
                aasta += "19"
            elif 5 <= int(n) <= 6:
                aasta += "20"
            elif 7 <= int(n) <= 8:
                aasta += "21"
        elif len(aasta) < 4:
            aasta += n
        elif len(kuu) < 2:
            kuu += n
        elif len(päev) < 2:
            päev += n

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
    elif kuu == "12":
        kuu = "detsember"
    
    sünd = päev + ". " + kuu + " " + aasta
    
    return sünd