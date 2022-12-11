from film import *

def töötleKäsk(käsk, sisu):
    if käsk == "K":
        str1 = ", "
        print("Võimalikud filmid on: " + str1.join(loetleFilmid(sisu)))
        return
    elif käsk == "L":
        sõna1 = ""
        for i in range(len(sisu)):
            if sisu[i] != " ":
                sõna1 += sisu[i]
            else:
                sõna2 = sisu[i+1:]
                break
        lisaFilm(sõna2, sõna1)
        print("Film lisatud!")
        return
    
    elif käsk == "V":
        kustutaFilm(sisu)
        print("Film nimekirjast kustutatud!\nHead vaatamist!")
        return
                
    
    
    
while True:
    sisend = input("""=== FILMIANDMEBAAS ===
    Kuva filmid: K <žanr>
    Lisa film:   L <žanr> <film>
    Vaata filmi: V <filmi nimi>
    Lõpeta:      E
    ===
    Sisestage soovitu: """)

    if sisend == "E":
        break
    
    töötleKäsk(sisend[0], sisend[2:])