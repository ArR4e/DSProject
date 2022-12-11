def sünnikuupäev(ik):
    kuud = ["jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
    sugu = int(ik[0])
    kuu = int(ik[3:5]) - 1
    päev = int(ik[5:7])
    if sugu == 1 or sugu == 2:
        aasta = str(18) + str(ik[1:3])
    elif sugu == 3 or sugu == 4:
        aasta = str(19) + str(ik[1:3])
    elif sugu == 5 or sugu == 6:
        aasta = str(20) + str(ik[1:3])
    else:
        print("Pole veel sündinud.")
    return str(päev) + ". " + kuud[kuu] + " " + str(aasta)
    