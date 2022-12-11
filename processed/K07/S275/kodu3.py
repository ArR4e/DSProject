def sünnikuupäev(x):
    numbrid = list(x)
    päev = str(numbrid[5]) + str(numbrid[6])
    if numbrid[0] == "1" or numbrid[0] == "2":
        aasta = (" 18" + str(numbrid[1] + numbrid[2]))
    elif numbrid[0] == "3" or numbrid[0] == "4":
        aasta = (" 19" + str(numbrid[1] + numbrid[2]))
    elif numbrid[0] == "5" or numbrid[0] == "6":
        aasta = (" 20" + str(numbrid[1] + numbrid[2]))
            
    kuu = str(numbrid[3]) + str(numbrid[4])
    if kuu == "01":
        kuud = (". jaanuar")
    elif kuu == "02":
        kuud = (". veebruar")
    elif kuu == "03":
        kuud = (". märts")
    elif kuu == "04":
        kuud = (". aprill")
    elif kuu == "05":
        kuud = (". mai")
    elif kuu == "06":
        kuud = (". juuni")
    elif kuu == "07":
        kuud = (". juuli")
    elif kuu == "08":
        kuud = (". august")
    elif kuu == "09":
        kuud = (". september")
    elif kuu == "10":
        kuud = (". oktoober")
    elif kuu == "11":
        kuud = (". november")
    elif kuu == "12":
        kuud = (". detsember")
    
    while True:
        try:
            return str(päev) + str(kuud) + str(aasta)
        except:
            break