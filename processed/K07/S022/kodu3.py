def sünnikuupäev(kood):
    koodlist = list(kood)
    paev = koodlist[5] + koodlist[6]
    kuu = koodlist[3] + koodlist[4]
    aasta = koodlist[1] + koodlist[2]
    sajand = koodlist[0]
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
    kuu = str(kuu)
    paev = str(paev)
    if sajand == "1" or sajand == "2":
        sajand = "18"
    if sajand == "3" or sajand == "4":
        sajand = "19"
    if sajand == "5" or sajand == "6":
        sajand = "20"
    sajand = str(sajand)
    aasta = str(aasta)
    kokku = sajand + aasta
    kuupaev = paev +". "+ kuu + ' ' + kokku
    return kuupaev
    
sünnikuupäev('5050618532')