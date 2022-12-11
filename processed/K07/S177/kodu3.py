isikukood=input("Sisesta oma isikukood: ")
def sünnikuupäev(isikukood):
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    
    sajand = isikukood[0]
    aastalõpp = isikukood[1:3]
    if sajand == "1" or sajand == "2":
        aasta = "18" + aastalõpp
    elif sajand == "3" or sajand == "4":
        aasta = "19" + aastalõpp
    else:
        aasta = "20" + aastalõpp
    
    kuu_indeks = int(isikukood[3:5])
    kuu = str (kuud[kuu_indeks - 1])
    kuupäev = isikukood[5:7]
    
    sünnipäev = kuupäev + ". " + kuu + " " + aasta
    return(sünnipäev)
    
print(sünnikuupäev(isikukood))
