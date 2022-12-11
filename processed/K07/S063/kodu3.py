###############################################################################################################
## Kirjuta funktsioon sünnikuupäev, mis võtab argumendiks Eesti isikukoodi sõnena ning tagastab               #
## sünnikuupäeva kujul <päev>. <kuu nimi> <aasta>.                                                            #
###############################################################################################################
def sünnikuupäev(id_sõne):
    # teisendame sõne järjendiks
    l = list(id_sõne)
    
    # koostame sünniaasta
    # esimene element on soo tunnus, millest sõltub sünniaasta õige kuju
    sugu = l[0]
    if sugu in ("1", "2"):
        aasta = "18"
    elif sugu in ("3", "4"):
        aasta = "19"
    elif sugu in ("5", "6"):
        aasta = "20"
    else:
        aasta = "21"
    aasta += l[1]+l[2]
    
    # koostame sünnikuu nime
    kuu = l[3]+l[4]
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni"]
    kuud += ["juuli", "august", "september", "oktoober", "november", "detsember"]
    # otsime vastavat kuunime kuude järjendist indeksi järgi
    for k in kuud:
        if int(kuu) ==  kuud.index(k) + 1:
            kuu_nimi = k
    
    # kuupäev 
    kuupäev = l[5]+l[6]
    # koostame ja tagastame tulemust õiges formaadis
    return("{0}. {1} {2}".format(kuupäev, kuu_nimi, aasta))
###############################################################################################################