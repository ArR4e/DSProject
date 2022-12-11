def sünnikuupäev(isikukood):
    esimene_nr = isikukood[0:1]
    teine_kolmas_nr = isikukood[1:3]
    neljas_viies_nr = isikukood[3:5] 
    kuues_seitsmes_nr = isikukood[5:7] + ". "
    if neljas_viies_nr == "01":
        kuu = "jaanuar "
    elif neljas_viies_nr == "02":
        kuu = "veebruar "
    elif neljas_viies_nr == "03":
        kuu = "märts "
    elif neljas_viies_nr == "04":
        kuu = "aprill "
    elif neljas_viies_nr == "05":
        kuu = "mai "
    elif neljas_viies_nr == "06":
        kuu = "juuni "
    elif neljas_viies_nr == "07":
        kuu = "juuli "
    elif neljas_viies_nr == "08":
        kuu = "august "
    elif neljas_viies_nr == "09":
        kuu = "september "
    elif neljas_viies_nr == "10":
        kuu = "oktoober "
    elif neljas_viies_nr == "11":
        kuu = "november "
    elif neljas_viies_nr == "12":
        kuu = "detsember "
        
    if esimene_nr == "1" or esimene_nr == "2":
        aasta = "18" + teine_kolmas_nr
    elif esimene_nr == "3" or esimene_nr == "4":
        aasta = "19" + teine_kolmas_nr
    elif esimene_nr == "5" or esimene_nr == "6":
        aasta = "20" + teine_kolmas_nr
        
    return kuues_seitsmes_nr + kuu + aasta
    
        
print(sünnikuupäev("60011302757"))