jaanuar = str("jaanuar")
veebruar = str("veebruar")
märts = str("märts")
aprill = str("aprill")
mai = str("mai")
juuni = str("juuni")
juuli = str("juuli")
august = str("august")
september = str("september")
oktoober = str("oktoober")
november = str("november")
detsember = str("detsember")

def sünnikuupäev(kood):
    return str(kood[5:7]) + ". " + str(kuud(kood))+ " " + str(aasta(kood)) + str(kood[1:3])
    
def aasta(a): 
    if int(a[0]) <= 2:
        return 18
    elif int(a[0]) <= 4:
        return 19
    elif int(a[0]) <= 6:
        return 20
    else:
        return "Viga" 

def kuud(c):
    if int(c[3]) == 0 and int(c[4]) == 1:
        return jaanuar
    elif int(c[3]) == 0 and int(c[4]) == 2:
        return veebruar
    elif int(c[4]) == 3:
        return märts
    elif int(c[4]) == 4:
        return aprill
    elif int(c[4]) == 5:
        return mai
    elif int(c[4]) == 6:
        return juuni
    elif int(c[4]) == 7:
        return juuli
    elif int(c[4]) == 8:
        return august
    elif int(c[4]) == 9:
        return september
    elif int(c[3:5]) == 10:
        return oktoober
    elif int(c[3:5]) == 11:
        return november
    elif int(c[3:5]) == 12:
        return detsember
      
print(sünnikuupäev("30107302740"))