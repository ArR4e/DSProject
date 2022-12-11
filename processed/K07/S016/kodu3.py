kuude_nimed = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]

def sünnikuupäev(isikukood):
    esimene_sümbol = isikukood[0]
    aasta = isikukood[1:3]
    if esimene_sümbol == "1" or esimene_sümbol == "2":
        aasta_päris = "18" + aasta
        päev = isikukood[5:7]
        kuu = isikukood[3:5]
        if päev[0] == "0":
            päev = päev[1]
            if kuu[0] == "0":
                kuu = kuu[1]
                kuu_arv = kuude_nimed[int(kuu)-1]
                return päev + ". " + kuu_arv + " " + aasta_päris
            else:
                kuu = kuude_nimed[int(kuu)-1]
                return päev + ". " + kuu + " " + aasta_päris
        else:
            if kuu[0] == "0":
                kuu = kuu[1]
                kuu_arv = kuude_nimed[int(kuu)-1]
                return päev + ". " + kuu_arv + " " + aasta_päris
            else:
                kuu = kuude_nimed[int(kuu)-1]
                return päev + ". " + kuu + " " + aasta_päris
    else:
        if aasta[0] == "0" or aasta[0] == "1" or aasta[0] == "2" or aasta[0] == "5":
            aasta_päris = "20" + aasta
        else:
            aasta_päris = "19" + aasta
        päev = isikukood[5:7]
        kuu = isikukood[3:5]
        if päev[0] == "0":
            päev = päev[1]
            if kuu[0] == "0":
                kuu = kuu[1]
                kuu_arv = kuude_nimed[int(kuu)-1]
                return päev + ". " + kuu_arv + " " + aasta_päris
            else:
                kuu = kuude_nimed[int(kuu)-1]
                return päev + ". " + kuu + " " + aasta_päris
        else:
            if kuu[0] == "0":
                kuu = kuu[1]
                kuu_arv = kuude_nimed[int(kuu)-1]
                return päev + ". " + kuu_arv + " " + aasta_päris
            else:
                kuu = kuude_nimed[int(kuu)-1]
                return päev + ". " + kuu + " " + aasta_päris


print(sünnikuupäev("19907062285"))