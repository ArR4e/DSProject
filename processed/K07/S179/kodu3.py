def sünnikuupäev(kood):
    a = list(kood)
    essa = a[0]
    aasta = a[1]+a[2]
    kuu = a[3]+a[4]
    päev = a[5]+a[6]
    if essa == "5" or essa == "6":
        aasta = "20"+aasta
    elif essa == "4" or essa == "3":
        aasta = "19"+aasta
    else:
        aasta = "18"+aasta
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
    
    return(f"{päev}. {kuu} {aasta}")