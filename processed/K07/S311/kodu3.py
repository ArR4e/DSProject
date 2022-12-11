def sünnikuupäev(kood):
    koodö = list(kood)
    aasta = 10*int(koodö[1])+int(koodö[2])
    if koodö[0] == "1" or koodö[0] == "2":
        aasta +=1800
    elif koodö[0] == "3" or koodö[0] == "4":
        aasta += 1900
    elif koodö[0] == "5" or koodö[0] == "6":
        aasta += 2000
    kuu = 10*int(koodö[3])+int(koodö[4])
    if kuu == 1:
        kuu = "jaanuar"
    elif kuu == 2:
        kuu = "veebruar"
    if kuu == 3:
        kuu = "märts"
    elif kuu == 4:
        kuu = "aprill"
    elif kuu == 5:
        kuu = "mai"
    elif kuu == 6:
        kuu = "juuni"
    elif kuu == 7:
        kuu = "juuli"
    elif kuu == 8:
        kuu = "august"
    elif kuu == 9:
        kuu = "september"
    elif kuu == 10:
        kuu = "oktoober"
    elif kuu == 11:
        kuu = "november"
    elif kuu == 12:
        kuu = "detsember"
    päev = int(koodö[5])*10+int(koodö[6])
    return "{}. {} {}".format(päev, kuu, aasta)  