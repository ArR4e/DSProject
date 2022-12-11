def sobivus(parool):
    numbrid = any(i.isdigit() for i in parool1)
    tähed = any(i.isalpha() for i in parool1)
    return numbrid and tähed

nimi = input('Sisestage kasutajanimi: ')

while True:
    parool1 = input('Sisestage parool: ')
    parool2 = input('Sisestage parool uuesti: ')
    pikkus=len(parool1)
    if parool1==parool2:
        if pikkus>=8:
            if sobivus(parool1):
                break
            else:
                print('Parool peab sisaldama nii tähti kui ka numbreid.')
        else:
            print('Parooli pikkus ei ole vähemalt 8 tähemärki')
    else:
        print('Paroolid ei ühti')
        
Parool=parool1[pikkus::-1]

fail = open('users.txt', 'w')
fail.write(nimi + ':' + Parool)

fail.close()

print('Kasutaja on loodud!')
