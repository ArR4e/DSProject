kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
def sünnikuupäev(isikukood):
    a = str(isikukood)
    for el in a:
        sajand = str(a[0])
        aasta = a[1:3]
        kuu = (int(a[3:5])-1)
        päev = a[5:7]
        if sajand == "1" or sajand == "2":
            aasta_arv = "18" + aasta
        elif sajand == "3" or sajand == "4":
            aasta_arv = "19" + aasta
        elif sajand == "5" or sajand == "6":
            aasta_arv = "20" + aasta
    print(päev + ". " + kuud[kuu] + " " + aasta_arv)