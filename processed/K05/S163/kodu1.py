kasutajanimi = str(input('Sisesta kasutajanimi: '))

while True:

    parool1 = str(input('Sisesta parool: '))
    parool2 = str(input('Sisesta parool uuesti: '))

    onTähed = False
    onNumbrid = False

    for i in parool1:
        try:
            i = int(i)
            onNumbrid = True
        except:
            onTähed = True

    if parool1 != parool2:
        print('Paroolid ei ühti')
        continue
    elif len(parool1) < 8:
        print('Parool peab olema vähemalt 8 tähemärki')
        continue
    elif onTähed == False or onNumbrid == False:
        print('Parool peab sisaldama nii tähti kui ka numbreid')
        continue
    else:
        break
    
tagurpidi = ''
for i in range(len(parool1)):
    tagurpidi += parool1[-1]
    parool1 = parool1[:-1]
    
fail = open('users.txt', 'w')
fail.write(kasutajanimi + ':' + tagurpidi + '\n')
fail.close()

print('Lõpp')

    

    
