def sünnikuupäev(x):
    a = ["jaanuar",'veebruar','märts','april','mai','juuni','juuli','august','september','oktoober','november','detsember']
    b = int(x[3:5])
    c = int(x[5:7])
    if x[0] == '1' or x[0] == '2':
        sajand = '18'
    elif x[0] == '3' or x[0] == '4':
        sajand = '19'
    elif x[0] == '5' or x[0] == '6':
        sajand = '20'
    aastanumber = sajand + x[1:3]
    return (str(c)+'. ' + str(a[b-1])+' '+str(aastanumber))
print(sünnikuupäev('34501234215'))
