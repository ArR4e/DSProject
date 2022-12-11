import film

def töötleKäsk(tahis, jarjend):
    if tahis == 'K':
        nimekiri = film.loetleFilmid(jarjend[0])
        try:
            print('Võimalikud filmid on:')
            for nimi in nimekiri:
                print(nimi)
        except:
            print('Selle žanri filme listis ei leidu')
        return True
        
    elif tahis == 'L':
        film.lisaFilm(jarjend[1], jarjend[0])
        print('Film lisatud!')
        return True
    
    elif tahis == 'V':
        film.kustutaFilm(jarjend[0])
        print('Print nimekirjast kustutatud!')
        return True
    
    elif tahis == 'E':
        return False
    
    
print('===FILMIANDMEBAAS===')
print('Kuva filmid: K <žanr>')
print('Lisa film:   L <žanr> <film>')
print('Vaata filmi: V <filmi nimi>')
print('Lõpeta:      E')
print('===')

while True:
    a = input()
    a = a.split(' ')
    töötleKäsk(a[0], a[1:])