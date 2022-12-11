def sünnikuupäev(kood):
    järjend = list(kood)
    kuupäev = "".join(järjend[5:7])
    
    kuu = "".join(järjend[3:5])
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

    aasta1 = "0"
    aasta2 = "".join(järjend[1:3])
    if järjend[0] in ["1", "2"]:
        aasta1 = "18"
    elif järjend[0] in ["3", "4"]:
        aasta1 = "19"
    elif järjend[0] in ["5", "6"]:
        aasta1 = "20"
    aasta = aasta1 + aasta2
    
    tulemus = kuupäev + ". " + kuu + " " + aasta
    return tulemus