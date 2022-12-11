#alustasin 26.09.2021 (22:37)
def check(parool):
    onnumbrit = False
    ontähte = False
    for i in parool:
        try:
            a = int(i)
            onnumbrit = True
        except:
            ontähte = True
    if onnumbrit and ontähte:
        return True
    else:
        return False
         
kasutajanimi = input('kasutajanimi: ')
while True:
    parool1 = input('parool: ')
    parool2 = input('Kirjutage sama parooli teist korda kinnituseks: ')
    if parool1 == parool2 and len(parool2) >= 8 and check(parool1):
        break
    else:
        print('Esimene parool peab kattuma teise parooliga.')
        print('Parooli sõne peab olema vähemalt 8 tähemärki pikk.')
        print('Sõnes te peate kasutama nii tähti kui numbreid.')

reverseparool = str(''.join(reversed(parool2)))
#funktsioon reversed pöörab mitte sõna (parool2) vaid selle sõna elemente eraldi
#ja funktsiooniga join liidame neid elemente tagasi, et meil ikka oleks pöördav sõna
fail = open('users.txt', 'w')
fail.write(kasutajanimi)
fail.write(':')
fail.write(reverseparool)
fail.close()