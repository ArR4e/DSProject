

def sünnikuupäev(isikukood):
    isikukood = list(isikukood)
    aasta_nr = "".join(isikukood[0:2])
    kuu_nr = "".join(isikukood[3:5])
    päeva_nr = isikukood[6:7]

    aasta = []
    kuu = "".join([kuu_nr])
    päev = []

        
    if aasta_nr[0] == "3" or "4":
        aasta += [19]
    else:
        aasta += [20]
        
    print(kuu_nr)
      

sünnikuupäev('34501234215')