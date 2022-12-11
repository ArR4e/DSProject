from film import loetleFilmid, lisaFilm, kustutaFilm

def töötleKäsk(käsk, järjend):
    if käsk == 'K':
        filmid = loetleFilmid(järjend[0].strip())
        print('Võimalikud filmid on:')
        for film in filmid:
            print(film)
        return True
    elif käsk == 'L':
        lisaFilm(järjend[1].strip(), järjend[0].strip())
        print('Film lisatud!')
        return True
    elif käsk == 'V':
        kustutaFilm(järjend[0].strip())
        print('Film nimekirjast kustutatud!\nHead vaatamist!')
        return True
    elif käsk == 'E':
        return False
    else:
        print('Tundmatu väärtus')

#while true loop
print("""=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
=== """)
while True:
    sisend = input()
    käsud = sisend.split(' ', 1)
    if käsud[0] == 'L':
        järjend = käsud[1].split(' ', 1)
    elif käsud[0] == 'E':
        järjend = []
    else:
        järjend = [käsud[1]]
    if not töötleKäsk(käsud[0], järjend):
        break
