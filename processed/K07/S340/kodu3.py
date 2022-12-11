def sünnikuupäev(isikukood):
    päev = isikukood[5:7]
    kuu = isikukood[3:5]
    kuude_järjend = ["jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
    kuu = kuude_järjend[int(kuu)-1]
    aasta = isikukood[1:3]
    if isikukood[0]==(3 or 4):
        aasta = "19" + str(aasta)
    else:
        aasta = "20" + str(aasta)
    print(päev+". "+kuu+" "+aasta)