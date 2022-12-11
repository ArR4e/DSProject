def sünnikuupäev(isikukood):
    kuu = int(isikukood[3:5])
    päev = int(isikukood[5:7])
    aasta = int(isikukood[1:3])
    esimene_nr = int(isikukood[0])
    if kuu == 1 and esimene_nr == 3 or kuu == 1 and esimene_nr == 4:
        return str(päev) + ". jaanuar " + str(aasta + 1900)
    elif kuu == 1 and esimene_nr == 5 or kuu == 1 and esimene_nr == 6:
        return str(päev) + ". jaanuar " + str(aasta + 2000)
    elif kuu == 1 and esimene_nr == 1 or kuu == 1 and esimene_nr == 2:
        return str(päev) + ". jaanuar " + str(aasta + 1800)
    elif kuu == 2 and esimene_nr == 3 or kuu == 2 and esimene_nr == 4:
        return str(päev) + ". veebruar " + str(aasta + 1900)
    elif kuu == 2 and esimene_nr == 5 or kuu == 2 and esimene_nr == 6:
        return str(päev) + ". veebruar " + str(aasta + 2000)
    elif kuu == 2 and esimene_nr == 1 or kuu == 2 and esimene_nr == 2:
        return str(päev) + ". veebruar " + str(aasta + 1800)
    elif kuu == 3 and esimene_nr == 3 or kuu == 3 and esimene_nr == 4:
        return str(päev) + ". märts " + str(aasta + 1900)
    elif kuu == 3 and esimene_nr == 5 or kuu == 3 and esimene_nr == 6:
        return str(päev) + ". märts " + str(aasta + 2000)
    elif kuu == 3 and esimene_nr == 1 or kuu == 3 and esimene_nr == 2:
        return str(päev) + ". märts " + str(aasta + 1800)
    elif kuu == 4 and esimene_nr == 3 or kuu == 4 and esimene_nr == 4:
        return str(päev) + ". aprill " + str(aasta + 1900)
    elif kuu == 4 and esimene_nr == 5 or kuu == 4 and esimene_nr == 6:
        return str(päev) + ". aprill " + str(aasta + 2000)
    elif kuu == 4 and esimene_nr == 1 or kuu == 4 and esimene_nr == 2:
        return str(päev) + ". aprill " + str(aasta + 1800)
    elif kuu == 5 and esimene_nr == 3 or kuu == 5 and esimene_nr == 4:
        return str(päev) + ". mai " + str(aasta + 1900)
    elif kuu == 5 and esimene_nr == 5 or kuu == 5 and esimene_nr == 6:
        return str(päev) + ". mai " + str(aasta + 2000)
    elif kuu == 5 and esimene_nr == 1 or kuu == 5 and esimene_nr == 2:
        return str(päev) + ". mai " + str(aasta + 1800)
    elif kuu == 6 and esimene_nr == 3 or kuu == 6 and esimene_nr == 4:
        return str(päev) + ". juuni " + str(aasta + 1900)
    elif kuu == 6 and esimene_nr == 5 or kuu == 6 and esimene_nr == 6:
        return str(päev) + ". juuni " + str(aasta + 2000)
    elif kuu == 6 and esimene_nr == 1 or kuu == 6 and esimene_nr == 2:
        return str(päev) + ". juuni " + str(aasta + 1800)
    elif kuu == 7 and esimene_nr == 3 or kuu == 7 and esimene_nr == 4:
        return str(päev) + ". juuli " + str(aasta + 1900)
    elif kuu == 7 and esimene_nr == 5 or kuu == 7 and esimene_nr == 6:
        return str(päev) + ". juuli " + str(aasta + 2000)
    elif kuu == 7 and esimene_nr == 1 or kuu == 7 and esimene_nr == 2:
        return str(päev) + ". juuli " + str(aasta + 1800)
    elif kuu == 8 and esimene_nr == 3 or kuu == 8 and esimene_nr == 4:
        return str(päev) + ". august " + str(aasta + 1900)
    elif kuu == 8 and esimene_nr == 5 or kuu == 8 and esimene_nr == 6:
        return str(päev) + ". august " + str(aasta + 2000)
    elif kuu == 8 and esimene_nr == 1 or kuu == 8 and esimene_nr == 2:
        return str(päev) + ". august " + str(aasta + 1800)
    elif kuu == 9 and esimene_nr == 3 or kuu == 9 and esimene_nr == 4:
        return str(päev) + ". september " + str(aasta + 1900)
    elif kuu == 9 and esimene_nr == 5 or kuu == 9 and esimene_nr == 6:
        return str(päev) + ". september " + str(aasta + 2000)
    elif kuu == 9 and esimene_nr == 1 or kuu == 9 and esimene_nr == 2:
        return str(päev) + ". september " + str(aasta + 1800)
    elif kuu == 10 and esimene_nr == 3 or kuu == 10 and esimene_nr == 4:
        return str(päev) + ". oktoober " + str(aasta + 1900)
    elif kuu == 10 and esimene_nr == 5 or kuu == 10 and esimene_nr == 6:
        return str(päev) + ". oktoober " + str(aasta + 2000)
    elif kuu == 10 and esimene_nr == 1 or kuu == 10 and esimene_nr == 2:
        return str(päev) + ". oktoober " + str(aasta + 1800)
    elif kuu == 11 and esimene_nr == 3 or kuu == 11 and esimene_nr == 4:
        return str(päev) + ". november " + str(aasta + 1900)
    elif kuu == 11 and esimene_nr == 5 or kuu == 11 and esimene_nr == 6:
        return str(päev) + ". november " + str(aasta + 2000)
    elif kuu == 11 and esimene_nr == 1 or kuu == 11 and esimene_nr == 2:
        return str(päev) + ". november " + str(aasta + 1800)
    elif kuu == 12 and esimene_nr == 3 or kuu == 12 and esimene_nr == 4:
        return str(päev) + ". detsember " + str(aasta + 1900)
    elif kuu == 12 and esimene_nr == 5 or kuu == 12 and esimene_nr == 6:
        return str(päev) + ". detsember " + str(aasta + 2000)
    elif kuu == 12 and esimene_nr == 1 or kuu == 12 and esimene_nr == 2:
        return str(päev) + ". detsember " + str(aasta + 1800)