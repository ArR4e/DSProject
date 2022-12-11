nimi = input("Sisestage kasutajanimi: ")

while True:
    #Küsime kasutajalt paroole kuni ta sisestab neid vastavalt reeglile
    parool = input('Sisestage parool: ')
    parool2 = input('Sisestage parool teist korda: ')
    
    #Kontrollime, kas paroolid kattuvad
    if parool != parool2:
        print('Esimene parool ei kattu teise parooliga!\n')
        
    #Kontrollime, kas parool on vähemalt 8 märki pikk
    elif len(parool) < 8:
        print("Valitud parool on liiga lühike!\n")
    
    #Toome sisse kontrollerid
    kontroll1 = 0
    kontroll2 = 0
    
    #Kontrollime, kas leiduvad paroolis numbrid
    for i in parool:
        numbrid = ['0','1','2','3','4','5','6','7','8','9']
        if i in numbrid:
            kontroll1 = 1
        #Samas kas leiduvad tähed
        else:
            kontroll2 = 1
            
    #Kui ei leidu kas ühtegi tähti või numbri, tagastatakse sõnum     
    if kontroll1 == 0 or kontroll2 == 0:
        print('Kasutage paroolis nii tähti kui numbreid!')
    #Jõuame siia, kui kõik tingimused on täidetud    
    else:
        break
    
parool = parool[::-1]
    
f = open('users.txt', 'w')
f.write(nimi + ':' + parool)
f.close()
