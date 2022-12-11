kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]


def sünnikuupäev(x):
    aasta = ""
    kuu = ""
    päev = ""
    if x[0]=="5" or x[0]=="6":
        aasta = 2000
    elif x[0]=="3" or x[0]=="4":
        aasta = 1900
    elif x[0]=="1" or x[0]=="2":
        aasta = 1800
    aasta = str(aasta + int(x[1:3]))
    kuu = kuud[int(x[3:5])-1]+" "
    päev = x[5:7]+". "
    kuupäev = str(päev) + str(kuu) + str(aasta)
    return kuupäev

print(sünnikuupäev("50107274244"))
       