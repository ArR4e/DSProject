def sünnikuupäev(isikukood):
    a = isikukood
    kuupäev = a[5:7]
    kuu = a[3:5]
    sünniaasta =a[1:3]
    aasta =a[0]
    if kuu == "01":
        k = "jaanuar"
    elif kuu == "02":
        k = "veebruar"
    elif kuu == "03":
        k = "märts"
    elif kuu == "04":
        k = "aprill"
    elif kuu == "05":
        k = "mai"
    elif kuu == "06":
        k = "juuni"
    elif kuu == "07":
        k = "juuli"
    elif kuu == "08":
        k = "august"
    elif kuu == "09":
        k = "september"
    elif kuu == "10":
        k = "oktoober"
    elif kuu == "11":
        k = "november"
    elif kuu == "12":
        k = "detsember"
    
    if aasta == "3":
        aasta_alg = "19"
    elif aasta ==  "4":
        aasta_alg = "19"
    elif aasta == "5":
        aasta_alg = "20"
    elif aasta == "6":
        aasta_alg = "20"
        
    return(kuupäev + ". " + k + " " + aasta_alg + sünniaasta)
        

