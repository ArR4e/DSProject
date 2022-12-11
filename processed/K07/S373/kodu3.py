def kuu(number):
    if number == 1:
        return "jaanuar"
    if number == 2:
        return "veebruar"
    if number == 3:
        return "märts"
    if number == 4:
        return "aprill"
    if number == 5:
        return "mai"
    if number == 6:
        return "juuni"
    if number == 7:
        return "juuli"
    if number == 8:
        return "august"
    if number == 9:
        return "september"
    if number == 10:
        return "oktoober"
    if number == 11:
        return "november"
    if number == 12:
        return "detsember"
    return None

def sünnikuupäev(isikukood):
    ilist = " ".join(isikukood).split()
    if int(ilist[0]) == 1 or int(ilist[0]) == 2:
        a = "18" + ilist[1] + ilist[2]
    elif int(ilist[0]) == 3 or int(ilist[0]) == 4:
        a = "19" + ilist[1] + ilist[2]
    else:
        a = "20" + ilist[1] + ilist[2]
    k = kuu(int(ilist[3] + ilist[4]))
    p = str(int(ilist[5] + ilist[6])) + "."
    return p + " " + k + " " + a
isikukood = (input("Sisestage oma isikukood: "))
print(sünnikuupäev(isikukood))
    