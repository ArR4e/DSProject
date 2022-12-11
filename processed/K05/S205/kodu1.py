def küsinime():
    global kasutajanimi
    kasutajanimi=str(input('Sisesta kasutajanimi: '))
    
def küsiparool():
    global krüpteeritud_parool
    parool=str(input('Sisesta parool: '))
    kontroll=str(input('Korda parooli: '))
    if parool != kontroll:
        print('Teine parool peab kattuma esimesega!')
        küsiparool()
    elif len(parool)<8:
        print('Parool peab olema vähemalt 8 tähemärki pikk!')
        küsiparool()
    elif any(char.isdigit() for char in parool) and any(char.isalpha() for char in parool):
        krüpteeritud_parool = parool[len(parool)::-1]
    else:
        print('Parool peab sisaldama vähemalt ühte tähte ja ühte numbrit!')
        küsiparool()
        


def registreering():
    küsinime()
    küsiparool()
    f = open('users.txt', 'a')
    f.write(kasutajanimi+':'+krüpteeritud_parool)
    
registreering()
    