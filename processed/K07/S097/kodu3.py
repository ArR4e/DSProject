def sünnikuupäev(isikukood):
    tühikutega_isikukood = ""
    for i in isikukood:
        tühikutega_isikukood += i
        tühikutega_isikukood += " "
        
    järjend = list(tühikutega_isikukood.split())
    
    #päev
    päev1nr = järjend[5]
    päev2nr = järjend[6]
    if päev1nr == "0":
        päev = päev2nr + "."
    else:
        päev = päev1nr + päev2nr + "."
        
    #kuu
    kuunr = "".join(järjend[3:5])
    if kuunr == "01":
        kuu = "jaanuar"
    elif kuunr == "02":
        kuu = "veebruar"
    elif kuunr == "03":
        kuu = "märts"
    elif kuunr == "04":
        kuu = "aprill"
    elif kuunr == "05":
        kuu = "mai"
    elif kuunr == "06":
        kuu = "juuni"
    elif kuunr == "07":
        kuu = "juuli"
    elif kuunr == "08":
        kuu = "august"
    elif kuunr == "09":
        kuu = "september"
    elif kuunr == "10":
        kuu = "oktoober"
    elif kuunr == "11":
        kuu = "november"
    else:
        kuu = "detsember"
        
    #aasta
    esimenenr = int(järjend[0])
    if esimenenr <= 2:
        aasta1osa = "18"
    elif esimenenr == 3 or esimenenr == 4:
        aasta1osa = "19"
    else:
        aasta1osa = "20"
    
    aasta2osa = "".join(järjend[1:3])
    aasta = aasta1osa + aasta2osa  
    päevkuuaasta = päev + " " + kuu + " " + aasta
    
    return päevkuuaasta

    