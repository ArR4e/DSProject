from film import loetleFilmid
from film import kustutaFilm
from film import lisaFilm
def töötleKäsk(tähis,järjend):
    if tähis == "K":
        if len(loetleFilmid(järjend)) > 0:
            for x in loetleFilmid(järjend):
                print(x)
        else:
            print("Selliseid filme pole")
        return True
    if tähis == "L":
        a=järjend.split(" ",1)
        print(a)
        lisaFilm(a[1],a[0])
        return True
    if tähis == "V":
        kustutaFilm(järjend)
        return True
    if tähis == "E":
        return False

while True:
    sisend=str(input(""))
    u=sisend.split(" ",1)
    if u[0]=="E":
        u.append("")
    print(u)
    if töötleKäsk(u[0],u[1]) == False:
        break