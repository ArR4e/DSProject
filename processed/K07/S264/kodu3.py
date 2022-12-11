
isikukood = str(input("Sisestage Eesti isikukood: "))
ik = list(isikukood)
kuude_järjend = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli",
                 "august", "september", "oktoober", "november", "detsember"]

def sünnikuupäev(isikukood):
    if int(ik[5]) == 0:
        kuupäev = int(ik[6])
    else:
        kuupäev = str(ik[5]) + str(ik[6])
    aasta = str(ik[1]) + str(ik[2])
    kuunr1 = int(ik[3])
    kuunr2 = int(ik[4])
    kokku = str(kuunr1) + str(kuunr2)
    if kuunr1 == 0:
        kuu = kuude_järjend[kuunr2 - 1]
    else:
        kuu = kuude_järjend[int(kokku) - 1]
    if int(ik[0]) == 1 or int(ik[0]) == 2:
        sajand = 18
    elif int(ik[0]) == 3 or int(ik[0]) == 4:
        sajand = 19
    elif int(ik[0]) == 5 or int(ik[0]) == 6:
        sajand = 20
    else:
        sajand = 21
    s = str(kuupäev) + ". " + str(kuu) + " " + str(sajand) + str(aasta)
    return s
    
print(sünnikuupäev(isikukood))
