kasutajanimi = input('Sisestage kasutajanimi: ')
parool = input('Sisestage parool: ')
parool2 = input('Sisestage parool uuesti palun: ')
tähed= False
numbrid= False
while True:
    if parool != parool2:
        print('Paroolid ei ole samad, proovi uuesti')
        continue
    elif len(parool) < 8:
        print('Parool peab olema vähemalt 8 sümbolit!')
        continue
    else:
        for sümbol in parool:
            if(sümbol.isdigit):
                numbrid=True
            if(sümbol.isalpha):
                tähed = True
        if numbrid and tähed:
            vastus = parool[::-1]
            break
        else:
            print('Paroolis puuduvasd kas tähed või numbrid!')
            continue
f = open("users.txt", "a")
f.write(kasutajanimi+":"+vastus)
f.close()
