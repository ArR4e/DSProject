from film import kustutaFilm
from film import lisaFilm
from film import loetleFilmid
def töötleKäsk(x, y):
    if xy.startswith("K") == True:
        jär = xy.split(" ")
        y = jär[1]
        z = loetleFilmid(y)
        print("Võimalikud filmid on:")
        for i in z:
            print(i)
        
    if xy.startswith("L") == True:
        jär = xy.split(" ", 2)
        y = jär[1]
        d = jär[2]
        z = lisaFilm(d, y)
        print("Film lisatud!")
    
    if xy.startswith("V") == True:
        jär = xy.split(" ", 1)
        y = jär[1]
        z = kustutaFilm(y)
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist!")
    if xy.startswith("E") == True:
        return False
        
while True:
    xy = input("")
    s = xy.split(" ", 2)
    x = s[0]
    try:
        y = s[1]
    except:
        break
    if töötleKäsk(x, y) == False:
        break
    
    
        

