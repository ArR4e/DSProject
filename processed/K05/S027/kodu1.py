nimi = str(input('Sisestage kasutajanimi: '))

while True:
    parool1 = str(input('Sisestage parool: '))
    parool2 = str(input('sisestage parool uuesti: '))
    if parool1 != parool2:
        print('Veateade: paroolid ei kattu.')#<>\
        continue
    elif len(parool2) < 8:
        print('Veateade: parool ei ole vähemalt 8 tähemärki')
    elif str.isdigit(parool2) or str.isalpha(parool2):
        print('Veateade: paroolis peab kasutama tähti ja numbreid')
        continue
    break
def krüptsioon(x):
    i = 0
    i1 = 1
    pikkus = len(x)
    kontroll = list(x)
    tagav = list(x)
    while pikkus - i > 0:
        kontroll[0+i] = str(tagav[pikkus-i1])
        i += 1
        i1 += 1
    parool = ''.join(kontroll)
    return parool
g = open('users.txt', 'w')
g.write(nimi + ':' + krüptsioon(parool2))
g.close()