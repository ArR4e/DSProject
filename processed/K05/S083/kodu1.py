def parool(p1, p2):
    while True:
        if p1 == p2:
            parool = p1
            if len(parool) >=8:
                numbrid = sum(c.isdigit() for c in parool)
                tähed = sum(c.isdigit() for c in parool)
                if numbrid > 0 and tähed > 0:
                    return parool
                else:
                    print('Paroolis peavad olema numbrid ja tähed.')
                    p1 = input('Sisestage parool: ')
                    p2 = input('Sisestage parool: ')
            else:
                print('Parool peab olema vähemalt 8 märki pikk.')
                p1 = input('Sisestage parool: ')
                p2 = input('Sisestage parool: ')
        else:
            print('Paroolid peavad kattuma.')
            p1 = input('Sisestage parool: ')
            p2 = input('Sisestage parool: ')
    
nimi = input('Sisestage kasutajanimi: ')
p1 = input('Sisestage parool: ')
p2 = input('Sisestage parool uuesti: ')

tagurpidi = parool(p1,p2)[::-1]
f = open('users.txt', 'w')
print(nimi + ':' + tagurpidi, file = f)
f.close()