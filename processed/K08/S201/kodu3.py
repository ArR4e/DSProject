from film import loetleFilmid
from film import lisaFilm
from film import kustutaFilm
def töötleKäsk(tähis, jarjend):
    if tähis == "K":
        if len(loetleFilmid(jarjend)) >0:
            for x in loetleFilmid(jarjend):
                print(x)
        else:
            print("Selliseid filme pole")
        return True
    if tähis == "L":
        koht = jarjend.split(" ",1)
        print(koht)
        lisaFilm(koht[1], koht[0])
        return True
    if tähis == "E":
        return False
while True:
    s = str(input(""))
    v = s.split(" ",1)
    if v[0] == "E":
        v.append("")
    print(v)
    if töötleKäsk(v[0],v[1]) == False:
        break
        
    
    
        