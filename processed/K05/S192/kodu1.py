kasutajanimi = input('Kasutajanimi: ')
parool_esimene = input('Esimene parool: ')
parool_teine = input('Korda sisestatud parooli: ')
while True:
    while parool_esimene != parool_teine:
        print('Esimene parool ei kattu teise parooliga')
        parool_esimene = input('Parool: ')
        parool_teine = input('Korda sisestatud parooli: ')
    while len(parool_esimene) < 8:
        print('Parool ei ole vähemalt 8 tähemärki pikk')
        parool_esimene = input('Parool: ')
        parool_teine = input('Korda sisestatud parooli: ')
    while parool_esimene.isalpha() == True:
        print('Parool ei sisalda numbreid')
        parool_esimene = input('Parool: ')
        parool_teine = input('Korda sisestatud parooli: ')
    pööratud_parool = parool_esimene[::-1] # Abi võetud: https://www.w3schools.com/python/python_howto_reverse_string.asp
    break
f = open('users.txt', 'w')
f.write(kasutajanimi + ':' + pööratud_parool)
f.close()