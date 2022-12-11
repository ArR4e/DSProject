#plokkskeem

kasutajanimi = input('Palun sisestage kasutajanimi: ')

#Tehniliselt ei vasta see kood plokkskeemile
#Plokkskeemiga võrreldes on siin niiöelda vastandküsimused
#Kui seal "Kas paroolid on samasugused?", siis siin "Kas nad ei ole samasugused?"
#Tundus, et niimoodi tuleb tulemus ilusam

while True:
    parool_1 = input('Palun sisestage parool: ')
    parool_2 = input('Palun sisestage parool uuesti: ')
    
    if not parool_1 == parool_2:
        print('Sisestatud paroolid on erinevad')
        continue
    elif len(parool_1) < 8:
        print('Paroolis on vähem kui 8 tähemärki')
        continue
    elif not (any(character.isdigit() for character in parool_1) and any(character.isalpha() for character in parool_1)): #https://stackoverflow.com/a/65358847
        print('Parool ei sisalda nii tähti kui ka numbreid')
        continue
    else:
        break
    
f = open('users.txt', 'w')
f.write(kasutajanimi + ':' + parool_1[::-1])
f.close()
