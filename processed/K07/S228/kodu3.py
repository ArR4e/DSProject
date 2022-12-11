def sünnikuupäev(isikukood):
    päev = isikukood[5:7]
    kuu = isikukood[3:5]
    kuu_järjend = ['jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli',\
                   'august', 'september', 'oktoober', 'november', 'detsember']
    kuu_indeks = int(kuu) - 1
    sünnikuu = kuu_järjend[kuu_indeks]
    sajand = int(isikukood[0])
    if 0 < sajand < 3:
        aasta = '18' + isikukood[1:3]
    elif 2 < sajand < 5:
        aasta = '19' + isikukood[1:3]
    elif 4 < sajand < 7:
        aasta = '20' + isikukood[1:3]
    inimese_sünnikuupäev = päev + ". " + sünnikuu + " " + aasta
    return inimese_sünnikuupäev

isikukood = input('Sisesta isikukood: ')
print(sünnikuupäev(isikukood))