import film as f

def töötleKäsk(tähis,järjend):
    
    if tähis == "K":
        loetelu = f.loetleFilmid(järjend[0])
        print("Võimaliku filmid on: ")
        for film in loetelu:
            print(film)
        return True
        
    if tähis == "L":
        f.lisaFilm(järjend[1],järjend[0])
        print("Film lisatud!")
        return True
        
        
    if tähis == "V":
        f.kustutaFilm(järjend[0])
        print("Film nimekirjast kustutatud! \n Head vaatamist!")
        return True
        
        
    if tähis == "E":
        return False
        
        
        
#Põhiprogramm
    
print("""Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E""")
järjend1 = []

while True:

    käsklus = input("").split(" ",1)
    esimene = käsklus[0]
    if käsklus[0] == "L":
        
        järjend1 = käsklus[1].split(" ",1)
    else:
        järjend1 = käsklus[1:]
    

    if töötleKäsk(käsklus[0],järjend1) == True:
        continue
    elif töötleKäsk(käsklus[0],järjend1) == False:
        break













    

