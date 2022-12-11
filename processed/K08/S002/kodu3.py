import film

def töötleKäsk(t,j):
    if t == "K":
        if film.loetleFilmid(j) == []:
            print("Neid filme pole")
        else:
            print("Võimalikud filmid: ")
            for i in film.loetleFilmid(j):
                print(i)
        return True
    elif t == "L":
        a = j.split()
        b = a[0]
        a.pop(0)
        film.lisaFilm(" ".join(a),b)
        print("Film lisatud")
        return True
    elif t == "V":
        film.kustutaFilm(j)
        print("Film kustutatud")
        return True
    elif t == "E":
        return False
    
while True:
    sisend = input(">")
    if töötleKäsk(sisend[0],sisend[2:]) == False:
        break