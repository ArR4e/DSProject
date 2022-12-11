from datetime import datetime

def sünnikuupäev(a):
    aasta = str(int(sajand(a))+int(a[1]+a[2]))
    sünnikuu = kuu(a[3]+a[4])
    kuupäev = (a[5]+a[6])
    sünnikuupäev = kuupäev+". "+sünnikuu+" "+aasta
    return sünnikuupäev

def sajand(a):
    sünniaasta = 0
    if a[0] == "1" or a[0] == "2":
        sünniaasta += 1800
    elif a[0] == "3" or a[0] == "4":
        sünniaasta += 1900
    elif a[0] == "5" or a[0] == "6":
        sünniaasta += 2000
    elif a[0] == "7" or a[0] == "8":
        sünniaasta += 2100
    return sünniaasta

def kuu(b):
    kuud = ["jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
    sünnikuu = kuud[int(b)-1]
    return sünnikuu
    