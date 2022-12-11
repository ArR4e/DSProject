# 3. Sünnikuupäev isikukoodist

def sünnikuupäev(isikukood):
    arvud = list(isikukood)
    kuupäev = ''.join(arvud[5:7]) + '.'
    kuud = ["jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
    kuu = kuud[int(''.join(arvud[3:5])) - 1]
    sajandid = ['18', '18', '18', '19', '19', '20', '20']
    aasta = sajandid[int(''.join(arvud[0:1]))] + ''.join(arvud[1:3])
    return(kuupäev + " " + kuu + " " + aasta)
    

isikukood = '34501234215'
sünnikuupäev(isikukood)
