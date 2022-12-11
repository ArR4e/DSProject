def sünnikuupäev(ID):
    if ID[0] == "1" or ID[0] == "2":
        aasta = 1800
    elif ID[0] == "3" or ID[0] == "4":
        aasta = 1900
    else:
        aasta = 2000
    aasta += int(ID[1:3])
    if ID[3:5] == "01":
        kuu = "jaanuar"
    elif ID[3:5] == "02":
        kuu = "veebruar"
    elif ID[3:5] == "03":
        kuu = "märts"
    elif ID[3:5] == "04":
        kuu = "aprill"
    elif ID[3:5] == "05":
        kuu = "mai"
    elif ID[3:5] == "06":
        kuu = "juuni"
    elif ID[3:5] == "07":
        kuu = "juuli"
    elif ID[3:5] == "08":
        kuu = "august"
    elif ID[3:5] == "09":
        kuu = "september"
    elif ID[3:5] == "10":
        kuu = "oktoober"
    elif ID[3:5] == "11":
        kuu = "november"
    else:
        kuu = "detsember"
    kuupäev = int(ID[5:7])
    return "{}. {} {}".format(kuupäev, kuu, aasta)