kasutajanimi=input('Sisestage kasutajanimi: ')

while True:
    parool1=input('Sisestage parool: ')
    parool2=input('Sisestage parool uuesti: ')
    
    if parool1!=parool2:
        print('Paroolid ei kattu!')
        continue
    elif len(parool1)<8:
        print('Parool peab olema vahemalt kaheksa tahemarki pikk!')
        continue
    elif parool1.isalpha()==True or parool1.isnumeric()==True:
        print('Parool peab sisaldama numbreid ja tahti!')
        continue
    else:
        break

umberpooratud=''.join(reversed(parool1))

f=open('users.txt','w')
f.write(kasutajanimi+':'+umberpooratud)
f.close()