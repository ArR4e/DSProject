def sünnikuupäev(a):
    kümnend = int(a[0])
    aasta = a[1:3]
    kuu = int(a[3:5])
    päev = int(a[5:7])
    kuud = ["", "jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    if kümnend == 1 or kümnend == 2:
        return (f"{päev}. {kuud[kuu]} 18{aasta}")
    elif kümnend == 3 or kümnend == 4:
        return (f"{päev}. {kuud[kuu]} 19{aasta}")
    elif kümnend == 5 or kümnend == 6:
        return (f"{päev}. {kuud[kuu]} 20{aasta}")
