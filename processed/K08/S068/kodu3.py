import film

def töötlekäsk(käsk,järjend):
     f=""
     c=0
     if käsk=="K":
        print("Võimalikud filmid on: ")
        while len(film.loetleFilmid(b)) >c:
            print(film.loetleFilmid(b)[c])
            c+=1
        return True
     elif käsk=="L":
         c=järjend[0]
         b=järjend[1]
         film.lisaFilm(c,b)
         print("Film lisatud!")
         return True
     elif käsk=="V":
         film.kustutaFilm(järjend)
         print("Film nimekirjast kustutatud!")
         print("Head vaatamist!")
         return True
     elif käsk=="E":
         return False
        
        
b=[]
print("=== FILMIANDMEBAAS ===")
print("Kuva filmid: K <žanr>")
print("Lisa film:   L <žanr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("Lõpeta:      E")
while True:
    a=input()
    a=a.split(" ")
    if len(a)==3:
        b.append(a[1])
        b.append(a[2])
        a=a[0]
    else:
        b=a[1]
        a=a[0]
    töötlekäsk(a,b)

