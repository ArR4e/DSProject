def sünnikuupäev(isikukood):
    aasta = isikukood[1:3]
    kuu = isikukood[3:5]
    päev = isikukood[5:7]
    if isikukood[0] == "1" or isikukood[0] == "2":
        if kuu == "01":
            return (päev + ". jaanuar 18" + aasta)
        if kuu == "02":
            return (päev + ". veebruar 18" + aasta)
        if kuu == "03":
            return (päev + ". märts 18" + aasta)
        if kuu == "04":
            return (päev + ". aprill 18" + aasta)
        if kuu == "05":
            return (päev + ". mai 18" + aasta)
        if kuu == "06":
            return (päev + ". juuni 18" + aasta)
        if kuu == "07":
            return (päev + ". juuli 18" + aasta)
        if kuu == "08":
            return (päev + ". august 18" + aasta)
        if kuu == "09":
            return (päev + ". september 18" + aasta)
        if kuu == "10":
            return (päev + ". oktoober 18" + aasta)
        if kuu == "11":
            return (päev + ". november 18" + aasta)
        if kuu == "12":
            return (päev + ". detsember 18" + aasta)
    elif isikukood[0] == "3" or isikukood[0] == "4":
        if kuu == "01":
            return (päev + ". jaanuar 19" + aasta)
        if kuu == "02":
            return (päev + ". veebruar 19" + aasta)
        if kuu == "03":
            return (päev + ". märts 19" + aasta)
        if kuu == "04":
            return (päev + ". aprill 19" + aasta)
        if kuu == "05":
            return (päev + ". mai 19" + aasta)
        if kuu == "06":
            return (päev + ". juuni 19" + aasta)
        if kuu == "07":
            return (päev + ". juuli 19" + aasta)
        if kuu == "08":
            return (päev + ". august 19" + aasta)
        if kuu == "09":
            return (päev + ". september 19" + aasta)
        if kuu == "10":
            return (päev + ". oktoober 19" + aasta)
        if kuu == "11":
            return (päev + ". november 19" + aasta)
        if kuu == "12":
            return (päev + ". detsember 19" + aasta)
    else:
        if kuu == "01":
            return (päev + ". jaanuar 20" + aasta)
        if kuu == "02":
            return (päev + ". veebruar 20" + aasta)
        if kuu == "03":
            return (päev + ". märts 20" + aasta)
        if kuu == "04":
            return (päev + ". aprill 20" + aasta)
        if kuu == "05":
            return (päev + ". mai 20" + aasta)
        if kuu == "06":
            return (päev + ". juuni 20" + aasta)
        if kuu == "07":
            return (päev + ". juuli 20" + aasta)
        if kuu == "08":
            return (päev + ". august 20" + aasta)
        if kuu == "09":
            return (päev + ". september 20" + aasta)
        if kuu == "10":
            return (päev + ". oktoober 20" + aasta)
        if kuu == "11":
            return (päev + ". november 20" + aasta)
        if kuu == "12":
            return (päev + ". detsember 20" + aasta)