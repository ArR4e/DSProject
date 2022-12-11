def sünnikuupäev(isikukood):
    kood = []
    kuud = ["","jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
    for el in isikukood:
        kood = kood + [el]
    aasta = "".join(kood[1:3])
    kuu = "".join(kood[3:5])
    paev = "".join(kood[5:7])
    kuunum = int(kuu)
    sajand = int(kood[0])
    if sajand == 5 or sajand == 6:
        aasta = "20" + aasta
    if sajand == 3 or sajand == 4:
        aasta = "19" + aasta
    if sajand == 1 or sajand == 2:
        aasta = "18" + aasta
    sünnipäev = "{0}. {1} {2}".format(paev, kuud[kuunum], aasta)
    return sünnipäev

    



