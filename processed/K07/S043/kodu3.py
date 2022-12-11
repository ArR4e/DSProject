kuud = ['jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', 'detsember']
def sünnikuupäev(isikukood):
    i = str(isikukood)
    kuu_nr = ""
    paev = ""
    kuu = ""
    if i[0] == '1' or i[0] == '2':
        aasta = '18'
    elif i[0] == '3' or i[0] == '4':
        aasta = '19'
    elif i[0] == '5' or i[0] == '6':
        aasta = '20'
    else:
        aasta = '21'
    aasta += i[1:3]
    kuu_nr += i[3:5]
    paev += i[5:7]
    kuu = kuud[int(kuu_nr)-1]
    return paev + ". " + kuu + " " + aasta

print(sünnikuupäev(35803120555))
