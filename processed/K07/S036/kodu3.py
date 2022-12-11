def sünnikuupäev(a):
    kuud = ["","jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
    if 2<int(a[0])<=4:
        aasta = "19" + a[1:3]
    elif int(a[0])<=2:
        aasta = "18" + a[1:3]
    else:
        aasta = "20" + a[1:3]
    kuu = kuud[int(a[3:5])]
    kuupäev = a[5:7]
    return (str(kuupäev) +". "+ kuu + " " + aasta)

print(sünnikuupäev('24501234215'))
