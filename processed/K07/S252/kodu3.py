def sünnikuupäev(isikukood):
    sünni_aasta = 0
    if isikukood[0] in ("1","2"):
        sünni_aasta = 1800
    if isikukood[0] in ("3","4"):
        sünni_aasta = 1900
    if isikukood[0] in ("5","6"):
        sünni_aasta = 2000

    aasta = int(isikukood[1:3])
    sünni_aasta += aasta
    sünni_kuu = isikukood[3:5]
    kuu_päev = isikukood[5:7]
    kuunimi = ""
    if sünni_kuu == "01":
        kuunimi = "Jaanuar"
    elif sünni_kuu == "02":
        kuunimi = "Veebruar"
    elif sünni_kuu == "03":
        kuunimi = "Märts"
    elif sünni_kuu == "04":
        kuunimi = "Aprill"
    elif sünni_kuu == "05":
        kuunimi = "Mai"
    elif sünni_kuu == "06":
        kuunimi = "Juuni"
    elif sünni_kuu == "07":
        kuunimi = "Juuli"
    elif sünni_kuu == "08":
        kuunimi = "August"
    elif sünni_kuu == "09":
        kuunimi = "September"
    elif sünni_kuu == "10":
        kuunimi = "Oktoober"
    elif sünni_kuu == "11":
        kuunimi = "November"
    elif sünni_kuu == "12":
        kuunimi = "Detsember"
    sünnikuupäev = str(kuu_päev) + "." + " " + kuunimi + " " + str(sünni_aasta)
    return(sünnikuupäev)
    
    
vastus = sünnikuupäev("34501234215")
print(vastus)