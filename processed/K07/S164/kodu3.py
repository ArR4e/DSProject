def sünnikuupäev(isikukood):
    vahemikud = [list(range(1800, 1900)), list(range(1800, 1900)), list(range(1900, 2000)), list(range(1900, 2000)), list(range(2000, 2100)), list(range(2000, 2100)), list(range(2100, 2200)), list(range(2100, 2200))]
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    
    päev = int(isikukood[5:7])
    kuu = kuud[int(isikukood[3:5])-1]
    sugu = int(isikukood[0])
    aasta = vahemikud[sugu-1][int(isikukood[1:3])]
    

    return "{0}. {1} {2}".format(päev, kuu, aasta)


print(sünnikuupäev("48112025210"))