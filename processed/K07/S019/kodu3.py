def sünnikuupäev(isikukood):
    isikukood2 = str(isikukood)
    error = ""
    if int(isikukood2[0]) == 3 or int(isikukood2[0]) == 4:
        saj = 1900
    elif int(isikukood[0]) == 5 or int(isikukood[0]) == 6:
        saj = 2000
    
    aasta = saj + int(isikukood2[1]) * 10 + int(isikukood[2])
    kuu = int(isikukood2[3]) * 10 + int(isikukood2[4])
    
    kuud = ["jaanuar","veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    kuu_sõne = kuud[kuu -1]
    
    päev = int(isikukood2[5]) * 10 + int(isikukood2[6])
    
    päev_punktiga = str(päev) + "."
    
    vastus = päev_punktiga + " " + kuu_sõne + " " + str(aasta)
    
    return vastus