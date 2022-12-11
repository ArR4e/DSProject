def aasta(kood):
    if int(kood[0]) == 1 or int(kood[0]) == 2:
        return 18
    if int(kood[0]) == 3 or int(kood[0]) == 4:
        return 19
    if int(kood[0]) == 5 or int(kood[0]) == 6:
        return 20
    
def kuu(kood):   
    if kood[3] == 0:
        kuu = kood[4]
    else:
        kuu = kood[3]+kood[4]
    kuud = ['kuu', 'jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', 'detsember']
    return kuud[int(kuu)] + ' '
    
def paev(kood):
    if kood[5] == 0:
        paev = kood[6]
    else:
        paev = kood[5]+kood[6]
    return paev + '. '
def sünnikuupäev(kood):
    aasta_nr = kood[1]+kood[2]
    return (paev(kood) + kuu(kood) + str(aasta(kood))+ str(aasta_nr))
   
sünnikuupäev('34501234215')