import re
user = input('Sisesta kasutajanimi: ')

while True: #Sisestame ja kontrollime parooli
    pass1 = input('Sisesta parool: ')
    pass2 = input('Sisesta parool teist korda: ')
    if not pass1 == pass2: #Kas esimene parool kattub teisega
        print('Paroolid ei kattu, proovi uuesti.')
        continue
    elif not len(pass1) >= 8: #Kas parool on vähemalt 8 tähemärki pikk
        print('Parool pole vähemalt 8 tähemärki pikk, proovi uuesti.')
        continue
    elif not re.search('\d', pass1) or not re.search('[a-zA-Z]', pass1): #Kas paroolis on kasutatud nii tähti kui numbreid
        print('Paroolis pole korraga tähti ja numbreid, proovi uuesti.')
        continue
    break

pass1 = pass1[::-1] #Pöörame parooli tagurpidi

f = open('users.txt', 'a') #Avame 'users' faili kasutaja lisamiseks
f.write(f'\n{user}:{pass1}') #Lisame uuele reale kasutajanime ja parooli
f.close()