
a = input("Sisestage isikukood: ")

def sünnikuupäev(a):
    kuud = ["jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
    kuunumber = int(a[3:5])
    kuu  = kuud[kuunumber -1]
    if a[0] == 6 or a[0] == 5:
        aasta = "20"+a[1:3]
        päev = a[5:7]
        väljund = (päev+". "+kuu+" "+aasta)
        return väljund
    else:
        aasta = "19"+a[1:3]
        päev = a[5:7]
        väljund = (päev+". "+kuu+" "+aasta)
        return väljund