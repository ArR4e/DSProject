def sünnikuupäev(isikukood):
    päev= str(isikukood[5:7])
    kuu = int(isikukood[3:5])
    kuu_järjend= ["jaanuar", "veebruar","märts","aprill","mai","juuni","juuli","\n"
                  "august","september","oktoober","november","detsember"]
    kuu= str(kuu_järjend[kuu-1])
    #sünniaasta = sajand +isikukood[1:3]
    sajand = int(isikukood[0])
    if sajand <3:
        sajand = 18
    elif 3 <=sajand <5:
        sajand = 19
    elif sajand >=5:
        sajand = 20
    sünniaasta = str(sajand)+isikukood[1:3]
    sünnikuupäev = päev +". "+ kuu + " "+ sünniaasta
    return sünnikuupäev
    
print(sünnikuupäev("34501234215"))