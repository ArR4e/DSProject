#sain abi konsulatsioonist ja murelahendajalt
def sünnikuupäev(isikukood):
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai",
            "juuni", "juuli", "august", "september",
            "oktoober", "november", "detsember"]
    kuu = int(isikukood[3:5])
    kuupäev = int(isikukood[5:7])
    aasta = int(isikukood[1:3])
    if aasta == 1 or aasta == 2:
        return "18"
    print(kuupäev, ". ", kuu, " ", "18", aasta)
    if aasta == 3 or aasta == 4:
        return "19"
    print(kuupäev, ". ", kuu, " ", "19", aasta)
    if aasta == 5 or aasta == 6:
        return "20"
    print(kuupäev, ". ", kuu, " ", "20", aasta)
    if aasta == 7 or aasta == 8:
        return "21"
    print(kuupäev, ". ", kuu, " ", "21", aasta)
