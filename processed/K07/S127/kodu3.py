def sünnikuupäev(isikukood):
    kuupäev =isikukood[5:7]
    kuu_nr=isikukood[3:5]
    kuude_järjend=["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    kuu=kuude_järjend[int(kuu_nr)-1]
    aasta=isikukood[1:3]
    if isikukood[0]==1 or isikukood[0]==2: #ma ei oska tervet aastaarvu väljastada
        aasta = "18" + isikukood[1:3]
    elif isikukood[0]==3 or isikukood[0]==4:
        aasta= "19"+isikukood[1:3]
    elif isikukood[0]==5 or isikukood[0]==6:
        aasta="20"+isikukood[1:3]
    
    sünnikuupäev = kuupäev + ". " + kuu + " " + str(aasta)
    return sünnikuupäev
vastus=sünnikuupäev("48906022754")
print(vastus)