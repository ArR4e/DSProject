isikukood = input("Sisesta isikukood: ")

def sünnikuupäev(isikukood):
    nimekiri = list(isikukood)
    
    päev = nimekiri[5] + nimekiri[6]
    
    
    kuunimekiri = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    kuunr = int(nimekiri[3] + nimekiri[4])
    kuunimi = kuunimekiri[kuunr-1]
    
    
    aastaalg = (int(isikukood[0]) + 1) // 2 + 17
    aasta = str(aastaalg) + nimekiri[1] + nimekiri[2]
    
    väljund = str(päev) + ". " + kuunimi + " " + aasta
    return väljund

print(sünnikuupäev(isikukood))