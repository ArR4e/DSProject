import film

while True:
    käsk = input('')
    if käsk == 'E':
        break
    järjend = input().split()
    töötleKäsk(käsk, järjend)
def töötleKäsk(käsk, järjend):
    if käsk == 'K':
        filmid = film.loetleFilmid(järjend)
        print("Võimalikud filmid on: \n" + filmid[0] + "\n" + filmid[1])
    elif käsk == 'L':
        film.lisaFilm(järjend[1], järjend[0])
    elif käsk == 'V':
        film.kustutaFilm(järjend)
        print('Film nimekirjast kustutatud!\nHead vaatamist!')
    