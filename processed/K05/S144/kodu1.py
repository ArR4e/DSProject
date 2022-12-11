nimi = str(input('Sisesta oma kasutajanimi: '))

def paroolikontroll(parool):
    if any(k.isdigit() for k in parool) and any(c.isalpha() for c in parool):
        return True
    else:
        return False
    
while True:
    parool1 = input('Sisesta oma parool: ')
    parool2 = input('Sisesta oma parool uuesti: ')
    if parool1 == parool2:
        if len(parool1) >= 8:
            if paroolikontroll:
                print('Parool sobib')
                break
            else:
                print('Parool ei sisalda nii numbreid kui ka tähti')
        else:
            print('Sisestatud parool ei ole vähemalt 8 tähemärki pikk')
            continue
    else:
        print('Sisestatud paroolid ei klapi')
        continue
    
parool_reversed = parool1 [::-1]
with open('users.txt','w') as f:
    f.write(f'{nimi}:{parool_reversed}')