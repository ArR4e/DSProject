def sünnikuupäev(isikukood):
    kuud = ["01", "jaanuar", "02", "veebruar", "03", "märts", "04", "aprill", "05", "mai", "06", "juuni", "07", "juuli",
            "08", "august", "09", "september", "10", "oktoober", "11", "november", "12", "detsember"]
    isikukood = list(isikukood)
    
    kuu = kuud[(kuud.index (isikukood[3] + isikukood[4]) ) +1]
    
    kuupäev = isikukood[5] + isikukood[6] 
    
    aasta_lõpp =(isikukood[1] + isikukood[2])
    if int(isikukood[0]) in range(1,3):
        aasta = "18" + aasta_lõpp
    elif int(isikukood[0]) in range(3,5):
        aasta = "19" + aasta_lõpp
    elif int(isikukood[0]) in range(5,7):
        aasta = "20" + aasta_lõpp
    
    
    return "{0}. {1} {2}".format(kuupäev, kuu, aasta) 
    

    
 

    

