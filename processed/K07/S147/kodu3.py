kuud = ["jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
def sünnikuupäev(isikukood):
    isikukood = list(isikukood)
    if isikukood[0] == "1" or isikukood [0] == "2":
        aasta = "18"
    elif isikukood[0] == "3" or isikukood[0] == "4":
        aasta = "19"
    else:
        aasta = "20"
    aasta += isikukood[1]+isikukood[2]
    kuu = isikukood[4]
    if isikukood[3] == "1":
        kuu = isikukood[3]+kuu
    if isikukood[5] == "0":
        päev = isikukood[6]
    else:
        päev = isikukood[5]+isikukood[6]
    return päev+". "+kuud[int(kuu)-1]+" "+aasta
print(sünnikuupäev(input("Sisestage oma isikukood: ")))