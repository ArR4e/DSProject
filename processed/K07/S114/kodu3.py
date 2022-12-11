aastaarv = 0
kuud = ["jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]    
kuupäev = 0
    
def sünnikuupäev(isikukood):
    if isikukood[0] == "1"or isikukood[0] == "2":
        aastaarv = "18"
    elif isikukood[0] == "3"or isikukood[0] == "4":
        aastaarv = "19"
    elif isikukood[0] == "5"or isikukood[0] == "6":
        aastaarv = "20"
    elif isikukood[0] == "7"or isikukood[0] == "8":
        aastaarv = "21"
    aastaarv = aastaarv + isikukood[1:3]
    kuu = int(isikukood[3:5])
    kuupäev = isikukood[5:7]
    vastus = kuupäev+". "+kuud[kuu-1]+" "+aastaarv
    return vastus

print(sünnikuupäev('70206234215'))
