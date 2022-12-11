nimi = input('Nimi: ')
while True:
    parool = input('Sisestage parool: ')
    parool_2 = input('Korrake parooli: ')
    n=0
    t=0
    for täht in parool:
        if täht.isnumeric():
            n=n+1
        else:
            t=t+1
    if parool != parool_2:
        print('Parool valesti sisestatud. Peate sisestama sama parooli kaks korda!')
        continue
    elif len(parool) < 8:
        print('Parool liiga lühike. Parooli pikkus peab olema vähemalt 8 tähemärki.')
        continue
    elif t ==0 or n ==0:
        print('Peate kasutama paroolis nii numbreid kui ka tähti.')
    else:
        break
parool = parool[::-1]
f = open('users.txt', 'w')
f.write(nimi+':'+parool)
f.close()