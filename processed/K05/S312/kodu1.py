#kontrolli kas on tähti ja numbreid
#allikas https://stackoverflow.com/questions/19859282/check-if-a-string-contains-a-number
def on_numbrid(x):
   return any(char.isdigit() for char in x)

def on_tähed(x):
    return any(char.isalpha() for char in x)

def pööra_tagurpidi(x):
    return x[::-1]

def faili():
    sisu = kasutajanimi + ':' + tagurpidi
    f = open('users.txt', 'w')
    f.write(sisu)
    f.close()


#põhiprogramm

kasutajanimi = str(input('Sisesta kasutajanimi: '))


while True:
    parool1 = str(input('Sisesta parool esimest korda: '))
    parool2 = str(input('Sisesta parool teist korda: '))
    if parool1 == parool2:
        if len(parool1) >= 8:
            if on_tähed(parool1) and on_numbrid(parool1):
                tagurpidi = pööra_tagurpidi(parool1)
                faili()
                print('Registreerimine oli edukas!')
                break
            else:
                print('Parool peab sisaldama nii tähti kui ka numbreid')
                
        else:
             print('Parool peab olema vähemalt 8 tähemärki pikk')
             
    else:
        print('Sisestatud paroolid ei klapi')
