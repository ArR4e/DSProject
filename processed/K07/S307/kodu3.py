### Järjendid, kus on kuude nimetused ja sajandid
kuud = ['jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november','detsember']
sajandid = ['18', '18','19','19', '20', '20', '21', '21', '22', '22']

### Funktsioon, mis leiab isikukoodist vajalikud andmed ja tagastab vastuse vajalikus vormis
def sünnikuupäev(str):
    vastus = ''
    sajandi_indeks = int(str[0]) #### Vajalik, et leida õige sajand
    sajand = sajandid[sajandi_indeks-1]
    aasta = str[1:3]
    kuupäev = str[5:7]
    kuu_indeks = 0
    if str[3] == '0': #### Vajalik, et saada õige indeks ka sellisel puhul, kui inimene on sündinud 01-09
        kuu_indeks = int(str[4])
    elif str[3] == '1':
        kuu_indeks = int(str[3:5])
    kuu = kuud[kuu_indeks -1]
    return vastus + kuupäev + '.' + ' ' + kuu + ' ' + sajand + aasta #### Vastus tahetud vormis


