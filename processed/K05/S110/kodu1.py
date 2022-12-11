user = input('Sisesta kasutajanimi: ')
pw = str(input('Sisesta parool: '))
pw2 = str(input('Sisesta parool uuesti: '))

if pw == pw2:
    if len(pw) >= 8: #vähemalt 8 märki
        if pw.isalnum():
            pw = pw[::-1] #pööra parool
            f = open('users.txt', 'w')
            f.write(user+':'+pw)
            f.close()
    else:
        print('Parool peab olema vähemalt 8 tähemärki')
else:
    print('Paroolid ei kattu või on puudulikud')