def sünnikuupäev(isikukood):
    jarjend = []
    kuunimed = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    for i in isikukood:
        jarjend = jarjend + [i]
    aasta = "".join(jarjend[1:3])
    paev = "".join(jarjend[5:7])
    kuupaev = "".join(jarjend[3:5])
    number = int(kuupaev) - 1
    if int(jarjend[0]) == 1 or int(jarjend[0]) == 2:
        taisaasta = "18" + aasta
    elif int(jarjend[0]) == 3 or int(jarjend[0]) == 4:
        taisaasta = "19" + aasta
    else:
        taisaasta = "20" + aasta
    sunnikuupaeva_kuju = "{0}. {1} {2}".format(paev, kuunimed[number], taisaasta)
    return sunnikuupaeva_kuju

