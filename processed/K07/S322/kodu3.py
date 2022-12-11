def sünnikuupäev(isikukood):
    # isikukoodilt aasta lugemine
    # 1. nr sajand (1 või 2 18xx, 3 või 4 19xx, 5 või 6 20xx jne)
    # 2. ja 3. nr aasta sajandil
    sajandjasugu = int(isikukood[0])
    # arvuta sajand valemiga
    aastatuhat = 1800 + int((sajandjasugu-1) / 2) * 100
    sünniaasta = isikukood[1:3]
    # eemalda aasta eest 0, kui see seal on
    if sünniaasta[0] == "0":
        sünniaasta = int(sünniaasta[1:])
    else:
        sünniaasta = int(sünniaasta)
    sünniaasta += aastatuhat
    # kuu lugemine
    kuud = ("jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember")
    kuu = isikukood[3:5]
    # eemalda kuu numbri eest 0, kui see seal on
    if kuu[0] == "0":
        kuu = kuud[int(kuu[-1])-1]
    else:
        kuu = kuud[int(kuu)-1]
    # kuupäeva lugemine
    päev = isikukood[5:7]
    # eemalda kuupäeva eest 0, kui see seal on
    if päev[0] == "0":
        päev = päev[-1]
    # tagasta
    return str(päev) + ". " + kuu + " " + str(sünniaasta)
