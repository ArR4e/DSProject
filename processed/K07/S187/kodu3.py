def sünnikuupäev(kood):
    if int(kood[0]) == 1 or int(kood[0]) == 2:
        aasta_esimesed = "18"
    elif int(kood[0]) == 3 or int(kood[0]) == 4:
        aasta_esimesed = "19"
    elif int(kood[0]) == 5 or int(kood[0]) == 6:
        aasta_esimesed = "20"
    elif int(kood[0]) == 7 or int(kood[0]) == 8:
        aasta_esimesed = "21"

    aasta_teised = kood[1:3]
    aasta = aasta_esimesed + aasta_teised
    kuu = kood[3:5]

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

    paev = kood[5:7]
    
    return(f"{paev}. {kuu} {aasta}")

print(sünnikuupäev('34501234215'))
