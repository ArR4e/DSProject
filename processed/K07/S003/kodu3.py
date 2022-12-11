def sünnikuupäev(isikukood):
    kuud = ["","jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
    if isikukood[0] == "1" or isikukood[0] == "2":
        aasta = "18"
    elif isikukood[0] == "3" or isikukood[0] == "4":
        aasta = "19"
    elif isikukood[0] == "5" or isikukood[0] == "6":
        aasta = "20"
    else:
        aasta = "21"
        
    
    aasta += isikukood[1:3]    
    kuu = kuud[int(isikukood[3:5])]
    kuupäev = isikukood[5:7]
    return kuupäev + ". " + kuu + " " + aasta
    
