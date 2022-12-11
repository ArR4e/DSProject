def sünnikuupäev(a):
    kuud = ["jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"] 
    b = list(a)
    if b[0] == "3" or b[0] == "4":
        aasta = "19" + b[1] + b[2]
    elif b[0] == "1" or b[0] == "2":
        aasta = "18" + b[1] + b[2]
    else:
        aasta = "20" + b[1] + b[2]
    kuu = kuud[int(b[3]+b[4])-1]
    päev = b[5] + b[6] + "."
    return päev + " " + kuu + " " + aasta

print(sünnikuupäev(input()))
