def sünnikuupäev(isikukood):
    sajand = isikukood[0]
    if sajand == "1" or sajand == "2":
        sünnisajand = "18"
    elif sajand == "3" or sajand == "4":
        sünnisajand = "19"
    elif sajand == "5" or sajand == "6":
        sünnisajand = "20"
        
    sünniaasta = isikukood[1] + isikukood[2]
    sünnikuu = isikukood[3] + isikukood[4]
    sünnikuupäev = isikukood[5] + isikukood[6]
    
    if sünnikuu == "01":
        sünnikuu = "jaanuar"
    elif sünnikuu == "02":
        sünnikuu = "veebruar"
    elif sünnikuu == "03":
        sünnikuu = "märts"
    elif sünnikuu == "04":
        sünnikuu = "aprill"
    elif sünnikuu == "05":
        sünnikuu = "mai"
    elif sünnikuu == "06":
        sünnikuu = "juuni"
    elif sünnikuu == "07":
        sünnikuu = "juuli"
    elif sünnikuu == "08":
        sünnikuu = "august"
    elif sünnikuu == "09":
        sünnikuu = "september"
    elif sünnikuu == "10":
        sünnikuu = "oktoober"
    elif sünnikuu == "11":
        sünnikuu = "november"
    elif sünnikuu == "12":
        sünnikuu = "detsember"

    return(sünnikuupäev + ". " + sünnikuu + " " + sünnisajand + sünniaasta)
sünnikuupäev('39910122345')
            