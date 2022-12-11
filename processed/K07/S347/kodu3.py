
def sünnikuupäev(isikukood):
    a = list(isikukood)
    if a[0] == "1" or a[0] == "2":
        aasta = str(f"18{a[1]}{a[2]}")
    if a[0] == "3" or a[0] == "4":
        aasta = str(f"19{a[1]}{a[2]}")
    if a[0] == "5" or a[0] == "6":
        aasta = str(f"20{a[1]}{a[2]}")
    if a[0] == "7" or a[0] == "8":
        aasta = str(f"21{a[1]}{a[2]}")
    kuunumber = f"{a[3]}{a[4]}"
    if kuunumber == "01":
        kuu = " jaanuar "
        päev = f"{a[5]}{a[6]}."
        return päev + kuu + aasta
    if kuunumber == "02":
        kuu = " veebruar "
        päev = f"{a[5]}{a[6]}."
        return päev + kuu + aasta
    if kuunumber == "03":
        kuu = " märts "
        päev = f"{a[5]}{a[6]}."
        return päev + kuu + aasta
    if kuunumber == "04":
        kuu = " aprill "
        päev = f"{a[5]}{a[6]}."
        return päev + kuu + aasta
    if kuunumber == "05":
        kuu = " mai "
        päev = f"{a[5]}{a[6]}."
        return päev + kuu + aasta
    if kuunumber == "06":
        kuu = " juuni "
        päev = f"{a[5]}{a[6]}."
        return päev + kuu + aasta
    if kuunumber == "07":
        kuu = " juuli "
        päev = f"{a[5]}{a[6]}."
        return päev + kuu + aasta
    if kuunumber == "08":
        kuu = " august "
        päev = f"{a[5]}{a[6]}."
        return päev + kuu + aasta
    if kuunumber == "09":
        kuu = " september "
        päev = f"{a[5]}{a[6]}."
        return päev + kuu + aasta
    if kuunumber == "10":
        kuu = " oktoober "
        päev = f"{a[5]}{a[6]}."
        return päev + kuu + aasta
    if kuunumber == "11":
        kuu = " november "
        päev = f"{a[5]}{a[6]}."
        return päev + kuu + aasta
    if kuunumber == "12":
        kuu = " detsember "
        päev = f"{a[5]}{a[6]}."
        return päev + kuu + aasta
print(sünnikuupäev("60104134210"))
