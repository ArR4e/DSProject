nimi = input('Kasutajanimi: ')
while True:
    parool = input('Parool: ')
    parool2 = input('Parool teist korda: ')
    Tähtede_Arv = 0
    Numbrite_Arv = 0
    if parool == parool2:
        if len(parool) >= 8:
            for sümbol in parool:
                if sümbol.isalpha():
                    Tähtede_Arv += 1
                elif sümbol.isdigit():
                    Numbrite_Arv += 1
            if Tähtede_Arv > 0 and Numbrite_Arv > 0:
                break
            else:
                print('Peab sisaldama nii tähti kui numbreid!')
                continue
        else:
            print('Parool peab olema vähemalt 8 tähemärki')
            continue
    else:
        print('Paroolid ei kattu!')
        continue

Vaese_krüpteering = parool[::-1]
f = open('users.txt', 'a')
f.write(nimi + ':' + Vaese_krüpteering)
f.close()

