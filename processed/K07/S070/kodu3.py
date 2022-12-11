def sünnikuupäev(kood):
    i = 0
    aasta = 0
    kuu = 0
    päev = 0
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    for number in kood:
        i += 1
        if i ==1:
            if int(number) < 3:
                aasta = 1800
            elif int(number) < 5:
                aasta = 1900
            elif int(number) >= 5:
                aasta = 2000
        if i == 2:
            aasta += int(number) * 10
        if i == 3:
            aasta += int(number)
        if i == 4:
            kuu = int(number) * 10
        if i == 5:
            kuu += int(number)
        if i == 6:
            päev = int(number) * 10
        if i == 7:
            päev += int(number)
    return str(päev) + ". " + kuud[kuu-1] + " " + str(aasta)
id =  input("    ")
print(sünnikuupäev(id))
        