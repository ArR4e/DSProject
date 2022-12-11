import film

def töötleKäsk(a, b):
    
    if b[0] == "K":
        
        print("Võimalikud filmid on:")
        nimed = film.loetleFilmid(b[1])
        for i in nimed:
            print(i)
        return True
        
    elif b[0] == "L":
        
        film.lisaFilm(b[2], b[1])
        print("Film lisatud!")
        return True
        
    elif b[0] == "V":
        
        film.kustutaFilm(b[1])
        print("Film nimekirjast kustutatud!\nHead vaatamist!")
        return True
        
    elif b[0] == "E":
        
        return False


a = ""
b = []
print("=== FILMIANDMEBAAS ===\nKuva filmid: K <žanr>\nLisa film:   L <žanr> <film>\nVaata filmi: V <filmi nimi>\nLõpeta:      E\n===")
a = input()
b = a.split(" ", 2)
töötleKäsk(b[0], b)

while b[0] != "E":
        a = input()
        b = a.split(" ", 2)
        töötleKäsk(b[0], b)