def sünnikuupäev(isikukood):
    kuud = {"jaanuar" :"01" , "veebruar": "02" , "märts" : "03", "aprill" : "04", "mai" : "05", "juuni" : "06", "juuli" :"07","august": "08", "september" :"09", "oktoober" :"10", "november" : "11", "detsember" : "12"}
    kuu = isikukood[3:5]
    sajand_18 = ["1","2"]
    sajand_19 = ["3", "4"]
    sajand_20 = ["5","6"]
    sajand_21 = ["7","8"]
    for i in kuud:
        if kuud[i] == kuu :
            kuu = i        
    päev = isikukood[5:7]
    if int(päev) < 10:
        päev = isikukood[6:7]
    else :
        päev = päev
    aasta = isikukood[1:3]
    if isikukood[0] in sajand_18:
        return päev + ". "+ kuu+ " 18" + aasta
    elif isikukood[0] in sajand_19:
        return päev + ". "+ kuu+ " 19" + aasta
    elif isikukood[0] in sajand_20:
        return päev + ". "+ kuu+ " 20" + aasta
    else:
        return päev + ". "+ kuu+ " 21" + aasta
print(sünnikuupäev("19907062285"))


    
