def sünnikuupäev(kood):
    kood=list(kood)   #jagab numbrid erinevateks listi liikmeteks
    kuu=["","jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
    if kood[0]=="3" or kood[0]=="4":
        aasta="19"+kood[1]+kood[2]
    elif kood[0]=="1" or kood[0]=="2":
        aasta="18"+kood[1]+kood[2]
    else:
        aasta="20"+kood[1]+kood[2]
    kuunimi=kuu[int(kood[3]+kood[4])]
    päev=int(kood[5]+kood[6])
    return f"{päev}. {kuunimi} {aasta}"