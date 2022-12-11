def sünnikuupäev(x):
    päev=x[5:7]
    kuu=int(x[3:5])
    nimetused = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    kuu_nimetus = nimetused[kuu-1]
    aasta=str(1900+int(x[1:3]))
    return(päev+". "+kuu_nimetus+" "+aasta)