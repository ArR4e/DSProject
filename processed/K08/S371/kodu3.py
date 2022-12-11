import film

sisend = input().split()

argumendid = []

if len(sisend) == 1:
    tähis = sisend[0]
if len(sisend) == 2:
    tähis = sisend[0]
    žanr = sisend[1]
    argumendid = žanr
if len(sisend) > 2:
    tähis = sisend[0]
    žanr = sisend[1]
    argumendid.append(žanr)
    sisend.pop(0)
    sisend.pop(0)
    nimi = ' '.join(map(str, sisend))
    argumendid.append(nimi)
    
def töötleKäsk(tähis, järjend):
        if tähis == "K":
            print(film.loetleFilmid(žanr))
            sisend = input().split()
        if tähis == "L":
            film.lisaFilm(žanr, nimi)
            print("Film lisatud!")
            sisend = input().split()
        if tähis == "V":
            film.kustutaFilm(nimi)
            print("Film nimekirjast kustutatud!")
            print("Head vaatamist!")
            sisend = input().split()
        else:
            return False

töötleKäsk(tähis, argumendid)

