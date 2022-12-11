import film as f
sisend=""
def töötleKäsk (tähis,järjend):
    if tähis=="K":
        asi=f.loetleFilmid(järjend[0])
        for a in asi:
            print(a)
        return True
    elif tähis=="L":
        f.lisaFilm(järjend[1],järjend[0])
        return True
    elif tähis=="V":
        f.kustutaFilm(järjend[0])
        return True
    elif tähis=="E":
        return False
while sisend !="E":
    sisend=input().split()
    töötleKäsk(sisend[0],sisend[1:])