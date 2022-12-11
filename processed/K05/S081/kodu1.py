def parooli_kontroll(a,b):
    if a == b:
        return True
    else:
        print('Paroolid ei klapi!')
        return False
    
def parooli_pikkus(a):
    if len(a) >= 8:
        return True
    else:
        print('Parool ei ole piisavalt pikk!')
        return False

def parooli_sisu(a):
    if any(i.isdigit() for i in a) and any(c.isalpha() for c in a):
        return True
    else:
        print('Paroolis puudub number või täht!')
        return False
    
#kasutajanimi
kn = input('Sisestage kasutajanimi: ')

#parool kontroll
while True:
    pw1 = input('Sisestage parool esimest korda: ')

    pw2 = input('Sisestage parool teist korda: ')
    
    if parooli_kontroll(pw1,pw2) and parooli_pikkus(pw1) and parooli_sisu(pw1):
        break
    else:
        continue
    
#krüpteerimine
parool = pw1[::-1]

fail = open('users.txt', 'a' )

fail.write(kn + ':' + parool + '\n')

fail.close()