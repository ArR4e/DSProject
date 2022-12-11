def sünnikuupäev(isikukood):
    päev = isikukood[5:7]
    if isikukood[5] == "0":
        päev = isikukood[6]
    
    kuu = isikukood[3:5]
    kuude_järjend = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    kuu_nimi = kuude_järjend[int(kuu)-1]
    
    esimene_nr = isikukood[0]
    aasta = isikukood[1:3]
    if esimene_nr == "1" or esimene_nr == "2":
        aasta = "18" + aasta
    elif esimene_nr == "3" or esimene_nr == "4":
        aasta = "19" + aasta
    else:
        aasta = "20" + aasta
        
    sünnikuupäev = päev + ". " + kuu_nimi + " " + aasta
    return sünnikuupäev
