def sünnikuupäev(isikukood):
    #5
    #01
    #02
    #12
    kood = str(isikukood)
    tuhat = 0
    aasta = str(kood[1:3])
    kuu = str(kood[3:5])
    paev = str(kood[5:7])
    if kood[0] == "3" or kood[0] == "4":
        tuhat += 19
    elif kood[0] == "5" or kood[0] =="6":
        tuhat += 20
    elif kood[0] == "1" or kood[0] == "2":
        tuhat += 18
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
        
    sunnipaev = (str(paev)+". "+str(kuu)+" "+str(tuhat)+str(aasta))
    return(sunnipaev)
sünnikuupäev(50107312726)
    