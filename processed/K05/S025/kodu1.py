def kattumine():
    parool_1 = str(input('Sisestage parool esimest korda: '))
    parool_2 = str(input('Sisestage parool teist korda: '))
    while parool_2 != parool_1:
        print('Paroolid ei kattu, palun proovige uuesti.')
        parool_1 = str(input('Sisestage parool esimest korda: '))
        parool_2 = str(input('Sisestage parool teist korda: '))
    global parool
    parool = parool_1

def pikkus():
    tähed = len(parool)
    while tähed < 8:
        print('Parool on liiga lühike, palun proovige uuesti.')
        kattumine()
        tähed = len(parool)

def numbrid_tähed():
    numbrid = sum(nr.isdigit() for nr in parool)
    tähed = sum(täht.isalpha() for täht in parool)
    if numbrid == 0 or tähed == 0:
        return False
    else:
        return True

kasutajanimi = str(input('Sisestage kasutajanimi: '))      
kattumine()
pikkus()
while numbrid_tähed() == False:
    print('Parool peab sisaldama nii tähti kui ka numbreid.')
    kattumine()
    pikkus()
    
tagurpidi = parool [::-1]
f = open('users.txt', 'a')
f.write(kasutajanimi + ':' + tagurpidi)
f.close()