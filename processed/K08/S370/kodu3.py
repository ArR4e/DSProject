from film import loetleFilmid,lisaFilm, kustutaFilm
def töötleKäsk(k, j):
    if k =="E":
        return False
    elif k=="K":
        print("Võimalikud filmid on:")
        print("\n".join(loetleFilmid("".join(j))))
        return True
    elif k=="L":
        lisaFilm(" ".join(j[1:]),j[0])
        print("Film lisatud!")
        return True
    elif k=="V":
        kustutaFilm(" ".join(j))
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist!")
        return True
        
        

print("=== FILMIANDMEBAAS ===")
print("Kuva filmid: K <žanr>")
print("Lisa film:   L <žanr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("Lõpeta:      E")
print("===")
a=True
while a==True:
    järjend=list(input().split(" "))
    käsk=järjend.pop(0)
    a= töötleKäsk(käsk, järjend)
    print("\n")
        
