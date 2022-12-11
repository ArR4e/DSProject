#isikukood = str(34501234215)

def sünnikuupäev(isikukood):
    aasta_lühike = str(isikukood[1:3])
    if int(isikukood[0]) < 3:
        aasta_pikk = "18" + aasta_lühike
    elif int(isikukood[0]) < 5:
        aasta_pikk = "19" + aasta_lühike
    elif int(isikukood[0]) < 7:  
        aasta_pikk = "20" + aasta_lühike
    kuu = int(isikukood[3:5])
    kuude_nimekiri = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    kuu_nimetus = str(kuude_nimekiri[kuu - 1])
    päev = str(isikukood[5:7])
    print(kuu)
    print(kuu_nimetus)
    print(aasta_lühike)
    print(aasta_pikk)
    print(päev)
    skp_sõnena = päev + ". " + kuu_nimetus + " " + aasta_pikk
    print(skp_sõnena)
    print(type(skp_sõnena))
    return str(skp_sõnena)
