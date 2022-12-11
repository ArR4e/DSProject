import string

print('Algus')

input('Sisesta kasutajanimi: ')
x = str(input('Sisesta parool: '))
y = str(input('Sisesta parool uuesti: '))

if x == y:
    print('Paroolid on samad.')
    
else:
    print('Paroolid ei ühildu.')
        
if len(x) >= 8:
    print('Sul on piisvalt tähemärke, liigu edasi.')

else:
    print('Kuid sinu parool pole piisavalt pikk.')
    
while True:

    if x.isnumeric:
        print('Parool peab sisaldama tähti ka.')
    
    if x.isalpha():
        print('Parool peab sisaldama numbreid ka.')
    else:
        print('Sul on nii tähed kui numbrid.')
        
    break



while True:
    print(reversed(x))

    break

    

    