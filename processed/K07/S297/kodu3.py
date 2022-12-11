isikukood = '34501234215'

def sünnikuupäev(isikukood) :
    järjend = list(isikukood)
    päev = ''.join(järjend[5:7])
    kuude_järjend = ['jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', 'detsember']
    if järjend[3] == '0' :
        kuu = kuude_järjend[(int(''.join(järjend[4]))- 1)]
    else :
        kuu = kuude_järjend[int(''.join(järjend[3:5]))]
    if järjend[0] == '5' or järjend[0] == '6' :
        aasta = '20' + ''.join(järjend[1:3])                         
    else :
        aasta = '19' + ''.join(järjend[1:3])
    return (f'{päev}. {kuu} {aasta}')

print(sünnikuupäev(isikukood))