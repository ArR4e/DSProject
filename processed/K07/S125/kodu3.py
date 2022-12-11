def sünnikuupäev(isikukood):
        #aastatuhat
    if int(isikukood[0]) in range(1,3):
        aastatuhat = "18"
    elif int(isikukood[0]) in range(3,5):
        aastatuhat = "19"
    elif int(isikukood[0]) in range(5,7):
        aastatuhat = "20"
    else:
        aastatuhat = "21"
    
    #aastakümmend
    aastakümmend = str(isikukood[1] + isikukood[2])
    
    sünniaasta = aastatuhat + aastakümmend
        
    #sünnikuu
    kuu = str(isikukood[3] + isikukood[4])
    
    if kuu == "01":
        sünnikuu = "jaanuar"
    elif kuu == "02":
        sünnikuu = "veebruar"
    elif kuu == "03":
        sünnikuu = "märts"
    elif kuu == "04":
        sünnikuu = "aprill"
    elif kuu == "05":
        sünnikuu = "mai"
    elif kuu == "06":
        sünnikuu = "juuni"
    elif kuu == "07":
        sünnikuu = "juuli"
    elif kuu == "08":
        sünnikuu = "august"
    elif kuu == "09":
        sünnikuu = "september"
    elif kuu == "10":
        sünnikuu = "oktoober"
    elif kuu == "11":
        sünnikuu = "november"
    elif kuu == "12":
        sünnikuu = "detsember"
    
    #kuupäev
    if isikukood[5] == "0":
        sünnikuupäev = str(isikukood[6])
    else:
        sünnikuupäev = str(isikukood[5] + isikukood[6])
    
    sünnikuupäev = "{0}. {1} {2}".format(sünnikuupäev, sünnikuu, sünniaasta)
    return sünnikuupäev

print(sünnikuupäev("16504150000"))   