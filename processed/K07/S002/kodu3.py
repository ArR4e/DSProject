kuud = ["jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
aasta = [18,18,19,19,20,20]
def sünnikuupäev(x):
    global kuud
    global aasta
    return str(x[5:7])+". "+str(kuud[int(x[3:5])-1])+" "+str(aasta[int(x[0])-1])+str(x[1:3])

print(sünnikuupäev('34501234215'))