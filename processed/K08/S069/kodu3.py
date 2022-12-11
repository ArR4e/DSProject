import film

print('Kuva filmid: K <žanr>')
print('Lisa film:   L <žanr> <film>')
print('Vaata filmi: V <filmi nimi>')
print('Lõpeta:      E')
sisend = input('sisesta käsk: ')
array = sisend.split()
käsk = array[0]
array.pop(0)
def töötleKäsk(täht, järjend):
    if täht == 'K':
        print('Võimalikud filmid on:')
        for sõna in film.loetleFilmid(järjend[0]):
            print(sõna)
           
    elif täht == 'L':
        liik = array[0]
        array.pop(0)
        nimi = ''.join(array)
        film.lisaFilm(nimi, liik)

    elif täht == 'V':
        print('Film nimekirjast kustutatud')
        print('Head vaatamist!')
        nimi = ' '.join(array)
        film.kustutaFilm(nimi)

    elif täht == 'E':
        return True
    
    sisend = input('Sisesta uus käsk: ')
    arrayUus = sisend.split()
    käsk = arrayUus[0]
    arrayUus.pop(0)
    töötleKäsk(käsk, arrayUus)
        
            
töötleKäsk(käsk, array)