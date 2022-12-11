def sünnikuupäev(isikukood):
    yy__ = isikukood[0]
    __yy = isikukood[1:3]
    mm = isikukood[3:5]
    päev = isikukood[5:7]
    
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli",
            "august", "september", "oktoober", "november", "detsember"]

    if yy__ in ["1","2"]:
        yy = "18"
    elif yy__ in ["3","4"]:
        yy = "19"
    elif yy__ in ["5","6"]:
        yy = "20"
    sajand = yy + __yy

    if len(mm) == 2 and mm[0] == "0":
        mm = mm[1]
    kuu = kuud[int(mm)-1]

    if len(päev) == 2 and päev[0] == "0":
        päev = päev[1]
        
    return " ".join([päev + ".", kuu, sajand])