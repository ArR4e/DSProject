aasta_algus = ''
kuud = ['jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', 'detsember']

def sünnikuupäev(isikukood):
    esimene_nr = isikukood[0]
    if esimene_nr == '1' or esimene_nr == '2':
        aasta_algus = '18'
    if esimene_nr == '3' or esimene_nr == '4':
        aasta_algus = '19'
    if esimene_nr == '5' or esimene_nr == '6':
        aasta_algus = '20'
    if esimene_nr == '7' or esimene_nr == '8':
        aasta_algus = '21'
    aasta_lõpp = isikukood[1:3]
    
    aasta = aasta_algus + aasta_lõpp
    kuu = kuud[int(int(isikukood[3:5]) - 1)]
    päev = isikukood[5:7]
    
    return (str(päev) + '. ' + kuu + ' ' + str(aasta))

print(sünnikuupäev('34501234215'))