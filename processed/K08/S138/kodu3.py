from film import loetleFilmid, lisaFilm, kustutaFilm

def töötleKäsk(tähis, sisend = []):
    if tähis == "K":
        print("Võimalikud filmid on:")
        for i in loetleFilmid(sisend[0]):
            print(i)
    elif tähis == "L":
        žanr = sisend.pop(0)
        sisend = " ".join(sisend)
        lisaFilm(sisend, žanr)
        print("Film lisatud!")
    elif tähis == "V":
        sisend = " ".join(sisend)
        kustutaFilm(sisend)
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist!")
            
    
print("=== FILMIANDMEBAAS ===")
print("Kuva filmid: K <žanr>")
print("Lisa film: L <žanr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("Lõpeta E")

while True:
    x = input()
    jär = x.split()
    x = jär.pop(0)
    if x == "E":
        break
    töötleKäsk(x, jär)
