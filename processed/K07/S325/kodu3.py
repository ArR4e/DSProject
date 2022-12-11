def sünnikuupäev(id):
    kuu=[0,"jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
    if id[0]=="4"or id[0]=="3":
        aasta = "19"
    elif id[0]=="1"or id[0]=="2":
        aasta = "18"
    else:
        aasta = "20"
    aasta+= id[1]+id[2]
    kuunr = int(id[3]+id[4])
    päev = int(id[5]+id[6])
    return (str(päev)+". "+kuu[kuunr]+" "+aasta)
sünnikuupäev("50108141514")