kuukood=("01", "jaanuar", "02", "veebruar","03","märts","04", "aprill", "05","mai", "06", "juuni","07","juuli","08","august","09","september", "10","oktoober", "11","november", "12", "detsember")
def sünnikuupäev(kood):
    päev=kood[5:7]
    kuu=kood[3:5]
    kuu=kuukood[kuukood.index(kuu)+1]
    aasta=kood[1:3]

    if kood[0] == "3" or kood[0] =="4":
        aasta="19"+aasta
    else:
        aasta="20"+aasta
    return päev+". "+kuu+" "+aasta

a= input("Sisesta isikukood: ")
print("Isiku sünnikuupäev on", sünnikuupäev(a))