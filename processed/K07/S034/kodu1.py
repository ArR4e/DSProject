def poisse_ja_tüdrukuid(järjend):
    #defineerime muutujad funktsiooni sees
    sõne = ""
    poiste_arv = 0
    tüdrukute_arv = 0
    #kõikide muutujate läbi vaatamiseks kasutame for tsüklit
    for rida in järjend:
        #leiame nende sood
        sõne = rida[-1]
        #loeme tüdrukute ja poiste arvud kokku
        if sõne == "P":
            poiste_arv += 1
        elif sõne == "T":
            tüdrukute_arv += 1
            #tagastame enniku
    return(poiste_arv, tüdrukute_arv)

